---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order Confirmation Amendment and Cancellation", "Redemption", "RedemptionBulkOrderConfirmationCancellationInstruction setr.053.001.03"]
content_origin: "source-transcription"
---

# RedemptionBulkOrderConfirmationCancellationInstruction setr.053.001.03

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order Confirmation Amendment and Cancellation / Redemption / RedemptionBulkOrderConfirmationCancellationInstruction setr.053.001.03.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3944** RedemptionBulkOrderConfirmationCancellationInstruction setr.053.001.03

**P3945** Description

**P3946** A RedemptionBulkOrderConfirmationCancellationInstruction is sent to cancel two previously sent redemption order confirmations.

**P3947** The first confirmed order for which the cancellation instruction is sent has reference order reference 1111 and deal reference 1111-0001.

**P3948** The second confirmed order for which the cancellation instruction is sent has reference order reference 2222 and deal reference 2222-0002.

**P3949** A RedemptionBulkOrderConfirmation (amendment) message will follow this cancellation instruction.

**P3950** Message Instance

**P3951** <RedBlkOrdrConfCxlInstr>

**P3952** 	<MsgId>

**P3953** 		<Id>R0022</Id>

**P3954** 		<CreDtTm>2026-01-05T14:30:30</CreDtTm>

**P3955** 	</MsgId>

**P3956** 	<AmdmntInd>true</AmdmntInd>

**P3957** 	<OrdrRefs>

**P3958** 		<OrdrRef>1111</OrdrRef>

**P3959** 		<DealRef>1111-0001</DealRef>

**P3960** 	</OrdrRefs>

**P3961** 			<OrdrRefs>

**P3962** 		<OrdrRef>2222</OrdrRef>

**P3963** 		<DealRef>2222-0002</DealRef>

**P3964** 	</OrdrRefs>

**P3965** </RedBlkOrdrConfCxlInstr>

