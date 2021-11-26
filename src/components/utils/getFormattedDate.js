export default function formatDate(date) {
    return `${new Date(date).getFullYear()}-${new Date(date).getDate()}-${new Date(date).getMonth()}`
}