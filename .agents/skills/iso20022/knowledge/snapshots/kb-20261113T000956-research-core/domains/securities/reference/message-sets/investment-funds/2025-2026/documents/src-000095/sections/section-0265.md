---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order Confirmation Amendment and Cancellation", "Subscription", "SubscriptionBulkOrderConfirmationCancellationInstruction setr.049.001.03"]
content_origin: "source-transcription"
---

# SubscriptionBulkOrderConfirmationCancellationInstruction setr.049.001.03

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order Confirmation Amendment and Cancellation / Subscription / SubscriptionBulkOrderConfirmationCancellationInstruction setr.049.001.03.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3904** SubscriptionBulkOrderConfirmationCancellationInstruction setr.049.001.03

**P3905** Description

**P3906** A SubscriptionBulkOrderConfirmationCancellationInstruction message is sent to cancel two previously sent subscription order confirmations.

**P3907** Confirmation 1

**P3908** The first confirmed order, for which the cancellation instruction is sent, has order reference 123-1 and deal reference 123-1/001. 

**P3909** Confirmation 2

**P3910** The second confirmed order, for which the cancellation instruction is sent, has order reference 123-2 and deal reference 123-2/002.

**P3911** A SubscriptionBulkOrderConfirmation (amendment) message will follow this cancellation instruction

**P3912** Message Instance

**P3913** <SbcptBlkOrdrConfCxlInstr>

**P3914** 	<MsgId>

**P3915** 		<Id>S0022</Id>

**P3916** 		<CreDtTm>2026-01-05T14:30:30</CreDtTm>

**P3917** 	</MsgId>

**P3918** 	<AmdmntInd>true</AmdmntInd>

**P3919** 	<OrdrRefs>

**P3920** 		<OrdrRef>123-1</OrdrRef>

**P3921** 		<DealRef>123-1/001</DealRef>

**P3922** 	</OrdrRefs>

**P3923** 	<OrdrRefs>

**P3924** 		<OrdrRef>123-2</OrdrRef>

**P3925** 		<DealRef>123-2/002</DealRef>

**P3926** 	</OrdrRefs>

**P3927** </SbcptBlkOrdrConfCxlInstr>

