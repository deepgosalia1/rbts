export default function formatDate(date) {
    return `${new Date(date).getFullYear()}-${new Date(date).getUTCMonth() + 1}-${new Date(date).getDate()}`
}