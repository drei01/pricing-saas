const colors = require('tailwindcss/colors');

module.exports = {
    content: ['./**/*.html', './**/*.md'],
    theme: {
        rotate: {
            120: '120deg',
            60: '60deg',
        },
        colors: {
            transparent: 'transparent',
            current: 'currentColor',
            black: colors.black,
            white: colors.white,
            gray: colors.neutral,
            green: colors.green,
            slate: colors.slate,
            fuchsia: colors.fuchsia,
            pink: colors.pink,
            blue: {
                50: '#f4f5f7',
                100: '#e8ebee',
                200: '#c7cdd5',
                300: '#a5aebc',
                400: '#617289',
                500: '#1d3557',
                600: '#1a304e',
                700: '#162841',
                800: '#112034',
                900: '#0e1a2b',
            },
            wedgewood: {
                50: '#f6f8fa',
                100: '#ecf2f5',
                200: '#d1dee7',
                300: '#b5cad8',
                400: '#7da3ba',
                500: '#457b9d',
                600: '#3e6f8d',
                700: '#345c76',
                800: '#294a5e',
                900: '#223c4d',
            },
            crimson: {
                50: '#fef5f6',
                100: '#fdebed',
                200: '#f9ced1',
                300: '#f5b0b5',
                400: '#ee747e',
                500: '#e63946',
                600: '#cf333f',
                700: '#ad2b35',
                800: '#8a222a',
                900: '#711c22',
            },
            'powder-blue': {
                50: '#fbfdfd',
                100: '#f6fbfc',
                200: '#e9f6f6',
                300: '#dcf0f1',
                400: '#c2e5e7',
                500: '#a8dadc',
                600: '#97c4c6',
                700: '#7ea4a5',
                800: '#658384',
                900: '#526b6c',
            },
            extend: {
                scale: {
                    '-100': '-1',
                },
                typography: ({ theme }) => ({
                    DEFAULT: {
                        css: {
                            code: {
                                backgroundColor: theme('colors.slate.100'),
                                borderRadius: theme('borderRadius.sm'),
                                paddingTop: theme('padding[1]'),
                                paddingRight: theme('padding[1.5]'),
                                paddingBottom: theme('padding[1]'),
                                paddingLeft: theme('padding[1.5]'),
                            },
                            'code::before': {
                                content: 'normal',
                            },
                            'code::after': {
                                content: 'normal',
                            },
                        },
                    },
                }),
            },
        },
    },
    plugins: [require('tailwindcss-highlights'), require('@tailwindcss/typography')],
};
