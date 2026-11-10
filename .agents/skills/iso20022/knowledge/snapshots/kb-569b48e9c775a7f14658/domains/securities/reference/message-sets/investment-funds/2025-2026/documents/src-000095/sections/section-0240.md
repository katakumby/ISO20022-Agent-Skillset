---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Subscription ", "SubscriptionBulkOrderCancellationRequest setr.008.001.05 "]
content_origin: "source-transcription"
---

# SubscriptionBulkOrderCancellationRequest setr.008.001.05 

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order and Confirmation / Subscription  / SubscriptionBulkOrderCancellationRequest setr.008.001.05 .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3063** SubscriptionBulkOrderCancellationRequest setr.008.001.05 

**P3064** Description

**P3065** A SubscriptionBulkOrderCancellationRequest message is sent to request the cancellation of two subscription orders.

**P3066** The first individual order to be cancelled has reference 123-1.

**P3067** The second individual order to be cancelled has reference 123-2.

**P3068** Message Instance

**P3069** <SbcptBlkOrdrCxlReq>

**P3070** 	<MsgId>

**P3071** 		<Id>S0002</Id>

**P3072** 		<CreDtTm>2026-01-04T09:30:30</CreDtTm>

**P3073** 	</MsgId>

**P3074** 	<OrdrRefs>

**P3075** 		<OrdrRef>123-1</OrdrRef>

**P3076** 	</OrdrRefs>

**P3077** 	<OrdrRefs>

**P3078** 		<OrdrRef>123-2</OrdrRef>

**P3079** 	</OrdrRefs>

**P3080** </SbcptBlkOrdrCxlReq>

