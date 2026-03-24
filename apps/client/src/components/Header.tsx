import { Text, makeStyles, tokens } from '@fluentui/react-components'
import { MoneyRegular } from '@fluentui/react-icons'

const useStyles = makeStyles({
  header: {
    display: 'flex',
    alignItems: 'center',
    height: '48px',
    paddingLeft: '16px',
    paddingRight: '16px',
    backgroundColor: '#010409',
    borderBottom: `1px solid ${tokens.colorNeutralStroke1}`,
    gap: '8px',
  },
  title: {
    color: '#ffffff',
    fontWeight: 600,
  },
  icon: {
    color: '#58a6ff',
    fontSize: '20px',
  },
})

export function Header() {
  const styles = useStyles()
  return (
    <header className={styles.header}>
      <MoneyRegular className={styles.icon} />
      <Text size={400} className={styles.title}>
        Contoso Finance
      </Text>
    </header>
  )
}
