---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order Confirmation Amendment and Cancellation", "Switch", "SwitchOrderConfirmationCancellationInstruction setr.055.001.03"]
content_origin: "source-transcription"
---

# SwitchOrderConfirmationCancellationInstruction setr.055.001.03

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order Confirmation Amendment and Cancellation / Switch / SwitchOrderConfirmationCancellationInstruction setr.055.001.03.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3967** SwitchOrderConfirmationCancellationInstruction setr.055.001.03

**P3968** Description

**P3969** A SwitchOrderConfirmationCancellationInstruction message is sent to cancel a previously sent switch order confirmation with order reference 20070103093512.

**P3970** A SwitchOrderConfirmation (amendment) message will not follow this cancellation instruction.

**P3971** Message Instance

**P3972** <SwtchOrdrConfCxlInstr>

**P3973** 	<MsgId>

**P3974** 		<Id>SW0020</Id>

**P3975** 		<CreDtTm>2026-01-03T16:30:30</CreDtTm>

**P3976** 	</MsgId>

**P3977** 	<AmdmntInd>true</AmdmntInd>

**P3978** 	<OrdrRefs>

**P3979** 		<OrdrRef>20070103093512</OrdrRef>

**P3980** 	</OrdrRefs>

**P3981** </SwtchOrdrConfCxlInstr>

