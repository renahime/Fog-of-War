import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getAllCategoriesThunk } from '../../store/category';
import { Link, NavLink } from "react-router-dom";
import "./HomePage.css";

export const grabHours = (stringDate) => {
	const dateInput = stringDate.slice(4);
	const stringDateObj = new Date(dateInput);
	const getMiliseconds = Math.abs(new Date() - stringDateObj);
	
}

function HomePage() {
	let date = new Date()
	const dispatch = useDispatch()
	let categories = useSelector(state => state.category.categories)
	let sessionUser = useSelector(state => state.session.user)
	let [loading, setLoading] = useState(false)
	let categoryArr = []

	useEffect(() => {
		dispatch(getAllCategoriesThunk()).then(() => setLoading(true))
	}, [dispatch])


	if (categories && (Object.values(categories).length > 1)) {
		categoryArr = Object.values(categories)
	}

	return (!loading && categoryArr.length < 1 ? <h1>Loading...</h1> :
		<div className='main-body'>
			<div className='main-topics-div'>
				<i class="fa-solid fa-film fa-2xl"></i>
				<i class="fa-solid fa-book fa-2xl"></i>
				<i class="fa-solid fa-wand-magic-sparkles fa-2xl"></i>
				<i class="fa-solid fa-gamepad fa-2xl"></i>
				<i class="fa-solid fa-tv fa-2xl"></i>
				<i class="fa-solid fa-clock fa-2xl"></i>
				<i class="fa-solid fa-comment fa-2xl"></i>
				<i class="fa-solid fa-bowl-food fa-2xl"></i>
				<i class="fa-solid fa-cat fa-2xl"></i>
				<center>
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
												<span className='font-awesome-space'></span>
											</div>
										</td>
										<td className='category-name-homepage'>
											<NavLink
												to={{
													pathname: `/${category.name}`,
													state: {
														category: category.name,
														categoryId: category.id,
													}
												}
												}>
												<strong>{category.name}</strong>
											</NavLink>
										</td>
										<td className='thread-count-homepage' >
											<strong >{category.thread_count}</strong>
										</td>
										<td className='post-count-homepage'>
											<strong>0</strong>
										</td>
										<td className='last-post-made-homepage'>
												<div style={{textAlign:'right', display:'flex', flexDirection:'column', gap:'9px', paddingRight:'7px', paddingTop:'7px', paddingBottom:'7px'}}>
												<strong className='subject-title'>
													{category.youngest_post.subject}
												</strong>
												<strong className='time-of-post'>
													Insert Time Here
												</strong>
												<strong className='post-author'>
												By: {category.youngest_post.user ? category.youngest_post.user.username : null}
												</strong>
												</div>
										</td>
									</tr>
									<div className='space-between-homepage'></div>
								</>
							))
						}
					</table>
				</center>
			</div>
		</div >
	);
}

export default HomePage
