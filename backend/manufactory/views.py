from django.shortcuts import render
from django.utils import timezone
from django.db.models import F
from authentication.models import UserAccount
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.permissions import (
    FabricationPermission,
    SubAssemblyPermission,
    AssemblyPermission,
    SuperAssemblyPermission,
    SuperFabricationPermission,
    SuperSubAssemblyPermission,
)
from .serializer import AssemblySerializer, FabricationSerializer, SubAssemblySerializer, MachineSerializer
from .models import Fabrication, SubAssembly, Assembly, Machine

from authentication.permissions import (
    FabricationPermission,
    SuperFabricationPermission,
    AssemblyPermission,
)

def get_user_from_request(request):
    # change this when auth is implemented

    _id = request.GET["id"]

    return CustomUser.objects.get(id=_id or 1)


# Fabiraction view
class FabricationDataView(APIView):
    permission_classes = (IsAuthenticated, FabricationPermission)
    def get(self, request):
        # Logic to retrieve Fabrication data
        # user = get_user_from_request(request)

        fabrications = Fabrication.objects.filter(out_date__isnull=True)
        serilizer = FabricationSerializer(fabrications, many=True)
        response_msg = {"quantity": fabrications.count(), "data": serilizer.data}

        response_code = 200

        return Response(response_msg, response_code)

    def post(self, request):
        # Logic to create a new Fabrication entry
        # Retrieve data from the request data
        item = request.data.get("item")
        raw_material = request.data.get("raw_material")
        quantity = request.data.get("quantity")
        # Create the new Fabrication entry
        new_fabrication = Fabrication.objects.create(
            item=item,
            raw_material=raw_material,
            quantity=quantity,
        )

        # Return a success response
        return Response(
            {"message": "Fabrication entry created successfully"}, status=201
        )

    # @permission_classes([SuperFabricationPermission])
    def patch(self, request):
        # Logic to update Assembly entry
        # Retrieve data from the request data
        self.permission_classes = SuperFabricationPermission
        id_list = request.data.get("id_list")

        # Retrieve the Assembly objects based on the specified IDs
        fabrications = Fabrication.objects.filter(item_id__in=id_list)

        # Update the old_date field to the current datetime
        current_datetime = timezone.now()
        # for assembly in fabrications:
        #     assembly.old_date = current_datetime

        # Prepare the bulk update data
        bulk_update_data = [
            Fabrication(item_id=assembly.item_id, old_date=current_datetime)
            for assembly in fabrications
        ]
        # print(bulk_update_data)
        # for a in bulk_update_data:
        #     print("cajknajnds", a.old_date)
        # Perform the bulk update
        Fabrication.objects.bulk_update(bulk_update_data, ["old_date"])
        print("aaya 1")
        return Response({"message": "Assembly updated successfully"}, status=201)

# SubAssenmbly
class SubAssemblyDataView(APIView):
    permission_classes = (IsAuthenticated, SubAssemblyPermission)
    def get(self, request):
        # Logic to retrieve SubAssembly data
        # user = get_user_from_request(request)

        subAssemblys = SubAssembly.objects.filter(end_date__isnull=True)
        serilizer = SubAssemblySerializer(subAssemblys, many=True)

        response_msg = {"quantity": subAssemblys.count(), "data": serilizer.data}

        response_code = 200

        return Response(response_msg, response_code)

    def post(self, request):
        # Logic to create a new SubAssembly entry
        # Retrieve data from the request data
        process = request.data.get("process")

        #get machin info
        machine_id = request.data.get("machine_id")
        # get fabrication info
        item_id = request.data.get("item_id")

        fabrication = Fabrication.objects.get(item_id=item_id) 
        machine = Machine.objects.get(id='machine_id')

        if not Fabrication or not machine:
            return Response({"message": "Invalid Id"},status=404)


        # Create the new SubAssembly entry
        new_SubAssembly = SubAssembly.objects.create(
            process=process,
            fabrication=fabrication,
            machine=machine_id
        )

        # Return a success response
        return Response(
            {"message": "SubAssembly entry created successfully"}, status=201
        )

    # SuperAssemblyPermission
    def patch(self, request):
        self.permission_classes = SuperSubAssemblyPermission
        # Logic to update Assembly entry
        # Retrieve data from the request data
        id_list = request.data.get("id_list")

        # Retrieve the Assembly objects based on the specified IDs
        assemblies = SubAssembly.objects.filter(assembly_id__in=id_list)

        # Update the end_date field to the current datetime
        current_datetime = timezone.now()
        # for assembly in assemblies:
        #     assembly.end_date = current_datetime

        # Prepare the bulk update data
        bulk_update_data = [
            SubAssembly(assembly_id=subassembly.assembly_id, end_date=current_datetime)
            for subassembly in assemblies
        ]
        print(bulk_update_data)
        for a in bulk_update_data:
            print("cajknajnds", a.end_date)
        # Perform the bulk update
        SubAssembly.objects.bulk_update(bulk_update_data, ["end_date"])
        print("aaya 1")
        return Response({"message": "SubAssembly updated successfully"}, status=201)

      


# Assembly
class AssemblyDataView(APIView):

    permission_classes = (IsAuthenticated, AssemblyPermission)
    def get(self, request):
        # Logic to retrieve Assembly data
        # user = get_user_from_request(request)

        assemblys = Assembly.objects.filter(end_date__isnull=True)
        serilizer = AssemblySerializer(assemblys, many=True)

        response_msg = {"quantity": assemblys.count(), "data": serilizer.data}

        response_code = 200

        return Response(response_msg, status=200)

    def post(self, request):
        # Logic to create a new Assembly entry
        # Retrieve data from the request data
        process = request.data.get("process")
        machine_id = request.data.get("machine_id")
        subassembly_id = request.get("subassembly_id")

        subassembly = Subassembly.objects.get(subassembly_id=subassembly_id) 
        machine = Machine.objects.get(id='machine_id')

        if not Fabrication or not machine:
            return Response({"message": "Invalid Id"},status=404)
        # Create the new Assembly entry
        new_assembly = Assembly.objects.create(
            machine=machine,
            subassembly=subassembly,
            process=process,
        )

        # Return a success response
        return Response({"message": "Assembly entry created successfully"}, status=201)

    # @permission_classes([SuperAssemblyPermission])
    def patch(self, request):
        self.permission_classes = SuperAssemblyPermission
        # Logic to update Assembly entry
        # Retrieve data from the request data
        id_list = request.data.get("id_list")

        # Retrieve the Assembly objects based on the specified IDs
        assemblies = Assembly.objects.filter(id__in=id_list)

        # Update the end_date field to the current datetime
        current_datetime = timezone.now()
        # for assembly in assemblies:
        #     assembly.end_date = current_datetime

        # Prepare the bulk update data
        bulk_update_data = [
            Assembly(id=assembly.id, end_date=current_datetime)
            for assembly in assemblies
        ]
        print(bulk_update_data)
        for a in bulk_update_data:
            print("cajknajnds", a.end_date)
        # Perform the bulk update
        Assembly.objects.bulk_update(bulk_update_data, ["end_date"])
        print("aaya 1")
        return Response({"message": "Assembly updated successfully"}, status=201)


## implement above in One view
# class UserDataView(APIView):
#     def get(self, request):


#         user = get_user_from_request(request)

#         fabrication_users = CustomUser.objects.filter(user_type="fabrication")
#         serilizer = FabricationSerializer(fabrications, many=True)

#         response_msg = {"data": serilizer.data}

#         response_code = 200
#         return Response(response_msg, response_code)


class ApprovedDataView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        # Logic to retrieve Fabrication data
        # user = get_user_from_request(request)

        fabrications = Fabrication.objects.filter(out_date__isnull=False)
        fabrications_data = FabricationSerializer(fabrications, many=True).data
        sub_assembly = SubAssembly.objects.filter(end_date__isnull=False)
        sub_assembly_data = SubAssemblySerializer(sub_assembly, many=True).data
        assembly = Assembly.objects.filter(end_date__isnull=False)
        assembly_data = AssemblySerializer(assembly, many=True).data

        response_msg = {
            "fabrications": {
                "quantity": fabrications.count(),
                "data": fabrications_data,
            },
            "sub_assembly": {
                "quantity": sub_assembly.count(),
                "data": sub_assembly_data,
            },
            "assembly": {"quantity": assembly.count(), "data": assembly_data},
        }

        response_code = 200

        return Response(response_msg, response_code)


class MachineListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        machines = Machine.objects.all()
        serializer = MachineSerializer(machines, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
