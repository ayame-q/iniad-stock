export const state = () => ({
	articles: [
		{
			uuid: '275d3b53-792e-240f-a470-de3298a13f49',
			title: 'Djangoを使ってWebアプリを作ってみた',
			text: `Djangoを使ってWebアプリを作ってみました。
## あばうと
DjangoでWebアプリを作ってみたんです。
\`\`\`python
print("やったね！！！")
\`\`\`
`,
			tags: [
				{ name: 'Python' },
				{ name: 'Django' },
			],
			user: {
				name: 'たろう',
				id: 'taro',
				icon: '/img/icon_sample.png',
			},
			time: '2021.7.11 22:40',
			comments: [
				{
					text: 'やったね',
					user: {
						name: '花子',
						id: 'hanako',
						icon: '/img/icon_sample.png',
					},
					time: '2021.7.12 10:40',
				},
				{
					text: 'おめでとう',
					user: {
						name: 'けん',
						id: 'ken',
						icon: '/img/icon_sample.png',
					},
					time: '2021.7.12 13:14',
				},
			],
		},
		{
			uuid: 'b3a6f6c1-0601-6a55-5ab4-40bc212b63c2',
			title: 'T-Car動かしてみた',
			text: 'T-Carが動いたの！！！',
			tags: [
				{ name: 'C' },
				{ name: 'T-Car' },
			],
			user: {
				name: '花子',
				id: 'hanako',
				icon: '/img/icon_sample.png',
			},
			time: '2021.7.8 12:40',
			comments: [
				{
					text: 'すごい！',
					user: {
						name: 'たろう',
						id: 'taro',
						icon: '/img/icon_sample.png',
					},
					time: '2021.7.12 10:40',
				},
			],
		},
		{
			uuid: 'b2a44c0b-1cf6-99c9-a827-eba68cc6cd83',
			title: '太陽、今日も昇る。',
			text: '2021年7月9日午前4時33分、東洋大学赤羽台キャンパスにて日の出が確認された。',
			tags: [
				{ name: 'SUN' },
			],
			user: {
				name: 'けん',
				id: 'ken',
				icon: '/img/icon_sample.png',
			},
			time: '2021.7.9 4:36',
			comments: [
				{
					text: '明けない夜はないんですね。感動しました。',
					user: {
						name: 'たろう',
						id: 'taro',
						icon: '/img/icon_sample.png',
					},
					time: '2021.7.9 8:22',
				},
			],
		},
		{
			uuid: '189c3a8b-c5ea-2b35-5821-06090de20af6',
			title: '赤羽台キャンパスで本当に旨い学食1選！',
			text: '東洋大学赤羽台キャンパスには学食が存在する。その中でも、オススメする店舗を紹介しよう。\n\n1. 糖朝\n\n油淋鶏丼が旨い。',
			tags: [
				{ name: 'Cafe' },
			],
			user: {
				name: '花子',
				id: 'hanako',
				icon: '/img/icon_sample.png',
			},
			time: '2021.7.10 12:11',
			comments: [
				{
					text: 'おいしそう・・・。',
					user: {
						name: 'けん',
						id: 'ken',
						icon: '/img/icon_sample.png',
					},
					time: '2021.7.12 0:51',
				},
			],
		},
		{
			uuid: 'b28ed916-c3af-a8f3-83b4-01188f2f6823',
			title: 'テスト前必見！　INIADの期末試験攻略',
			text: 'もうすぐやってくる期末のシーズン。試験本番で重要なポイントをまとめた。これで君もオールSだ！\n\n1. 試験前にノートパソコンの充電を満タンにしておく。\n\n大事な大事な試験中にバッテリー切れ、なんてことになったら目も当てられない。ノートパソコンの充電をしっかりしておこう。',
			tags: [
				{ name: 'Exam' },
			],
			user: {
				name: 'たろう',
				id: 'taro',
				icon: '/img/icon_sample.png',
			},
			time: '2021.7.11 19:26',
			comments: [
				{
					text: '助かります！',
					user: {
						name: '花子',
						id: 'hanako',
						icon: '/img/icon_sample.png',
					},
					time: '2021.7.12 4:32',
				},
			],
		},
	],
})

export const mutations = {
	add (state, article) {
		state.articles.push(article)
	},
}

export const getters = {
	getAll (state) {
		return state.articles
	},
	getMine (state, uuid) {
		state.articles.find((element) => {
			return element.user.name === 'たろう'
		})
	},
}

export const actions = {
}
