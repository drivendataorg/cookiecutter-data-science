/* Smooth scrolling for termynal replay */

function scrollToBottomOfContainer(container, element) {
    var positionToScroll = element.offsetTop + element.offsetHeight - container.offsetHeight;
    container.scrollTo({
        top: positionToScroll,
        behavior: 'smooth'
    });
}

// Select the node that will be observed for mutations
const targetNode = document.getElementById("termynal");

// Options for the observer (which mutations to observe)
const config = { attributes: false, childList: true, subtree: false };

// Callback function to execute when mutations are observed
const callback = (mutationList, observer) => {
  for (const mutation of mutationList) {
    scrollToBottomOfContainer(targetNode, mutation.target);
  }
};

// Create an observer instance linked to the callback function
const observer = new MutationObserver(callback);

// Start observing the target node for configured mutations
observer.observe(targetNode, config);
