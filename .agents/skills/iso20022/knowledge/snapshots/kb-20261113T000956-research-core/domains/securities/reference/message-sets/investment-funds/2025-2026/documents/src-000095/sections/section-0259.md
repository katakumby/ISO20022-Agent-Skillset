---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order Status", "OrderCancellationStatusReport setr.017.001.05"]
content_origin: "source-transcription"
---

# OrderCancellationStatusReport setr.017.001.05

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order Status / OrderCancellationStatusReport setr.017.001.05.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3831** OrderCancellationStatusReport setr.017.001.05

**P3832** Description

**P3833** An OrderCancellationStatusReport message is sent to report on the status of a cancellation request. It reports that the order with order reference Order 15 is pending cancellation.

**P3834** Message Instance

**P3835** <OrdrCxlStsRpt>

**P3836** 	<MsgId>

**P3837** 		<Id>OC001</Id>

**P3838** 		<CreDtTm>2026-01-10T09:30:30</CreDtTm>

**P3839** 	</MsgId>

**P3840** 	<StsRpt>

**P3841** 		<IndvCxlStsRpt>

**P3842** 			<OrdrRef>Order 15</OrdrRef>

**P3843** 			<CxlSts>

**P3844** 				<Sts>CANP</Sts>

**P3845** 			</CxlSts>

**P3846** 		</IndvCxlStsRpt>

**P3847** 	</StsRpt>

**P3848** </OrdrCxlStsRpt>

