import {useRecoilValue} from 'recoil';
import {isLoggedIn, userData} from '../../atoms'
import { Navigate, Outlet, useLocation } from 'react-router-dom';

const ProtectedRoutes = ({ allowedRoles }) => {
    const user = useRecoilValue(userData);
    const LoggedIn = useRecoilValue(isLoggedIn);
    const location = useLocation();

    return (
        (user?.user_type) === allowedRoles
            ? <Outlet />
            : LoggedIn
                ? <Navigate to="/unauthorized" state={{ from: location }} replace />
                : <Navigate to="/login" state={{ from: location }} replace />
    )
}

export default ProtectedRoutes;