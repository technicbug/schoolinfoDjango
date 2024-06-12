const list = document.getElementById('list');


const searchInput = document.getElementById('search');
const searchBtn = document.getElementById('searchButton');


async function loadImages(loc_num) {
  const response = await fetch(`/getmap/images/?loc_num=${loc_num}`);
  if (response.ok) {
      const images = await response.json();
      
      console.log(images);  // 응답 데이터 확인을 위한 로그 출력

      const container = document.getElementById('image-container');
      container.innerHTML = '';  // Clear previous images

      images.forEach(image => {
          const imgElement = document.createElement('img');
          imgElement.src = image.image;  // 이미지 URL 사용
          imgElement.alt = image.loc_num;  // 적절한 alt 텍스트 설정
          container.appendChild(imgElement);
      });
  } else {
      console.error('Failed to load images:', response.statusText);
  }
}

function detail(name ='', loc='', locNum='', clear = false){
    const mapimg = document.getElementById('map');
    if(clear == true){
        mapimg.innerHTML = '';
    } else{
        mapimg.innerHTML = '';
        mapimg.innerHTML = `
            <h2>${name} | ${loc}</h2>
            
            <div id="image-container"></div> <!-- 여기에 이미지가 표시될 컨테이너 추가 -->
        `;
        loadImages(locNum);
    }
}
