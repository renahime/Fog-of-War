import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getAllCategoriesThunk } from '../../store/category';
import { Link, NavLink } from "react-router-dom";
import "./HomePage.css";

export const grabHours = (stringDate) => {
	if (!stringDate)
		return

	const dateInput = stringDate;
	const stringDateObj = new Date(dateInput);
	const currentTime = new Date();
	const getMiliseconds = Math.abs(currentTime.getTime() - stringDateObj.getTime());
	const hours = getMiliseconds / (1000 * 60 * 60)

	if (hours > 24) {
		const days = Math.floor(getMiliseconds / (1000 * 60 * 60 * 24))
		return `${days} days ago`
	} else if (hours < 1) {
		const minutes = Math.floor(getMiliseconds / (1000 * 60))
		return `${minutes} minutes ago`
	} else {
		return `${Math.floor(hours)} hours ago`
	}
}


function HomePage() {
	let date = new Date()
	const dispatch = useDispatch()
	let categories = useSelector(state => state.category.categories)
	let sessionUser = useSelector(state => state.session.user)
	let [loading, setLoading] = useState(false)
	let categoryArr = []

	const handleAlert = (e) => {
		alert("More seeds comning soon!")
	}

	const getIconForCategory = (categoryName) => {
		if (categoryName == "Movies")
			return <i class="fa-solid fa-film fa-2xl"></i>
		if (categoryName == "Literature")
			return <i class="fa-solid fa-book fa-2xl"></i>
		if (categoryName == "Anime Manga and VNs")
			return <i class="fa-solid fa-wand-magic-sparkles fa-2xl"></i>
		if (categoryName == "Video Games")
			return <i class="fa-solid fa-gamepad fa-2xl"></i>
		if (categoryName == "TV Shows")
			return <i class="fa-solid fa-tv fa-2xl"></i>
		if (categoryName == "History")
			return <i class="fa-solid fa-clock fa-2xl"></i>
		if (categoryName == "Religion and Philosophy")
			return <i class="fa-solid fa-comment fa-2xl"></i>
		if (categoryName == "Food")
			return <i class="fa-solid fa-bowl-food fa-2xl"></i>
		if (categoryName == "Pets")
			return <i class="fa-solid fa-cat fa-2xl"></i>
	}

	useEffect(() => {
		dispatch(getAllCategoriesThunk()).then(() => setLoading(true))
	}, [dispatch])


	if (categories && (Object.values(categories).length > 1)) {
		categoryArr = Object.values(categories)
	}
	return (!loading || categoryArr.length < 1 ? <h1>Loading...</h1> :
		<div className='main-body'>
			<table className='main-page-table'>
				<thead>
					<td colSpan={5} className='topic-title'>
						<strong>Topic</strong>
					</td>
				</thead>
				<tbody>
					<td colSpan={2} className='forum-title'>
						<strong>Forum</strong>
					</td>
					<td className='threads-title'>
						<strong>Threads</strong>
					</td>
					<td className='posts-title'>
						<strong>Posts</strong>
					</td>
					<td className='last-post-title'>
						<strong>Last Post</strong>
					</td>
				</tbody>
				{
					categoryArr.map((category) => (
						<>
							<div className='space-between-homepage'></div>
							<tr className='home-page-table-row'>
								<td style={{ verticalAlign: 'middle' }} className='font-awesome-placement'>
									<div className='font-awesome-space'>
										{getIconForCategory(category.name)}
									</div>
								</td>
								<td className='category-name-homepage'>
									{category.name !== "Anime Manga and VNs" ? <strong className='non-seed' onClick={handleAlert}>{category.name}</strong> : <NavLink
										to={{
											pathname: `/${category.name}`,
											state: {
												category: category.name,
												categoryId: category.id,
											}
										}
										}>
										<strong>{category.name}</strong>
									</NavLink>}
								</td>
								<td className='thread-count-homepage' >
									<strong >{category.thread_count}</strong>
								</td>
								<td className='post-count-homepage'>
									<strong>{category.post_count}</strong>
								</td>
								<td className='last-post-made-homepage'>
									{category.youngest_post.category ? <NavLink
										to={{
											pathname: `/${category.youngest_post.category.name}/${category.youngest_post.subcategory.name}/threads/${category.youngest_post.thread_id}`,
											state: {
												category: category.youngest_post.category.name,
												categoryId: category.youngest_post.category.id,
												subcategory: category.youngest_post.subcategory.name,
												subcategoryId: category.youngest_post.subcategory.id,
												threadId: category.youngest_post.thread_id
											}
										}}>
										<div style={{ textAlign: 'right', display: 'flex', flexDirection: 'column', gap: '9px', paddingRight: '7px', paddingTop: '7px', paddingBottom: '7px' }}>
											<strong className='subject-title'>
												{category.youngest_post.thread_subject ? category.youngest_post.thread_subject : category.youngest_post.subject}
											</strong>
											<strong className='time-of-post'>
												{category.youngest_post ? grabHours(category.youngest_post.created_at) : null}
											</strong>
											<strong className='post-author'>
												By: {category.youngest_post.user ? category.youngest_post.user.username : null}
											</strong>
										</div>
									</NavLink>
										: null}
								</td>
							</tr>
							<div className='space-between-homepage'></div>
						</>
					))
				}
			</table>
		</div >
	);
}

export default HomePage
