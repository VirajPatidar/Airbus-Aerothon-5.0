import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import { styled } from '@mui/material/styles';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';


const StyledTableCell = styled(TableCell)(({ theme }) => ({
    [`&.${tableCellClasses.head}`]: {
        backgroundColor: theme.palette.common.black,
        color: theme.palette.common.white,
    },
    [`&.${tableCellClasses.body}`]: {
        fontSize: 14,
    },
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
    '&:nth-of-type(odd)': {
        backgroundColor: theme.palette.action.hover,
    },
    // hide last border
    '&:last-child td, &:last-child th': {
        border: 0,
    },
}));



export default function GlobalStamped({ tableData }) {

    return (
        <TableContainer component={Paper}>
            <Table sx={{ minWidth: 200 }} aria-label="simple table">
                <TableHead>
                    <TableRow>
                        <StyledTableCell>Item ID</StyledTableCell>
                        <StyledTableCell>Item</StyledTableCell>
                        <StyledTableCell>Raw Material</StyledTableCell>
                        <StyledTableCell>Quantity</StyledTableCell>
                        <StyledTableCell>In Date</StyledTableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {tableData.map((row, idx) => (
                        <StyledTableRow
                            key={idx}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                            >
                            <StyledTableCell component="th" scope="row">{row.item_id}</StyledTableCell>
                            <StyledTableCell component="th" scope="row">{row.item}</StyledTableCell>
                            <StyledTableCell>{row.raw_material}</StyledTableCell>
                            <StyledTableCell>{row.quantity}</StyledTableCell>
                            <StyledTableCell>{row.in_date}</StyledTableCell>
                        </StyledTableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}