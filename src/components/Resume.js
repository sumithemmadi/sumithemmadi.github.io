import { Viewer, Worker ,SpecialZoomLevel} from '@react-pdf-viewer/core';
// import { defaultLayoutPlugin } from '@react-pdf-viewer/default-layout';

import '@react-pdf-viewer/core/lib/styles/index.css';
import '@react-pdf-viewer/default-layout/lib/styles/index.css';

export default function MyApp() {
    return (
        <Worker workerUrl="https://unpkg.com/pdfjs-dist@3.4.120/build/pdf.worker.js">
            <div style={{ height: '100vh' }}>
                <Viewer
                    fileUrl={`${process.env.PUBLIC_URL}/MaskedResume.pdf`}
                    plugins={[]}
                    defaultScale={SpecialZoomLevel.PageFit}
                />
            </div>
        </Worker>
    );
}
