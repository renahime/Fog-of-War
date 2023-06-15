import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getAllCategoriesThunk } from '../../store/category';
import { Link } from "react-router-dom";
import "./HomePage.css";

function HomePage() {
	let date = new Date()
	const dispatch = useDispatch()
	let categories = useSelector(state => state.category.category)
	let sessionUser = useSelector(state => state.session.user)
	let [loading, setLoading] = useState(false)
	let categoryArr = []

	useEffect(() => {
		dispatch(getAllCategoriesThunk()).then(() => setLoading(true))
	}, [dispatch])


	if (categories && (Object.values(categories).length > 1)) {
		categoryArr = Object.values(categories)
	}

	console.log(categoryArr)


	return (categoryArr.length < 1 ? <h1>Loading...</h1> :
		<div className='main-body'>
			<div className='main-topics-div'>
				<div className='header-topic'>
					<h6>Main Topics</h6>
				</div>
				<div className='column-names'>
					<h6>Forum</h6>
					<h6>Threads</h6>
					<h6>Posts</h6>
					<h6>Last Post</h6>
				</div>
				{categoryArr.map((category) => (
					<div className='category-name'>
						{category.name}
					</div>
				))}
			</div>
		</div>
	);
}

export default HomePage
