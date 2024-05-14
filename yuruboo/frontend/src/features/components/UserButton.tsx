import Fab from '@mui/material/Fab';
import Icon from '@mui/material/Icon';
import AccountCircleRoundedIcon from '@mui/icons-material/AccountCircleRounded'; 

import { styled } from '@mui/material/styles';

type Props = {
	onToggleUserInfo: () => void;
};

const FabButton = styled(Fab)({
	position: 'fixed',
	right: 15,
	top: 15,
	disableRipple: true,
	zIndex: 10000,
});

export const UserButton: React.FC<Props> = ({ onToggleUserInfo }) => {
	return (
	<FabButton
		sx={{
			backgroundColor: "#ffffff",
			'&:hover': {
				backgroundColor: "ffffff",
			},
			'&:active': {
				backgroundColor: "#ffffff",
			},
		}}
		onClick={onToggleUserInfo}>
		<Icon sx= {{width: '100%', height: '100%'}}>
                <AccountCircleRoundedIcon sx= {{fontSize: 56}} /> {/* AccountCircleRoundedアイコンの表示 */}
        </Icon>

	</FabButton>
	);
};