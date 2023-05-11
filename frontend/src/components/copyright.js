//MUI
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';

export default function Copyright() {
	return (
		<Typography variant="body2" color="textSecondary" align="center" sx={{ mt: 4, mb: 4 }} >
			{'Copyright © '}
			<Link color="inherit" href="https://github.com/VirajPatidar/Airbus-Aerothon-5.0">
				A320
			</Link>{' '}
			{new Date().getFullYear()}
			{'.'}
		</Typography>
	);
}