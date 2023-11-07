import './globals.css'
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import { ThemeProvider } from "@/components/ThemeProvider"
import Navbar from '@/components/Navbar'


const inter = Inter({ subsets: ['latin'] })


export const metadata: Metadata = {
  title: 'Crypto Chain',
  description: 'Developed with ❤️ by DevAdeel',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <>
      <html lang="en" suppressHydrationWarning>
        <head />
        <body>
          <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
            <Navbar/>
            {children}
          </ThemeProvider>
        </body>
      </html>
    </>
  )
}
