---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Transfer Cancellation", "TransferInCancellationRequest sese.006.001.09"]
content_origin: "source-transcription"
---

# TransferInCancellationRequest sese.006.001.09

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Transfer Cancellation / TransferInCancellationRequest sese.006.001.09.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P5123** TransferInCancellationRequest sese.006.001.09

**P5124** Description

**P5125** A TransferInCancellationRequest is sent by the new plan manager (transferee), PEFIGB2, to the executing party, the transfer agent, to request the cancellation of a previously sent TransferInInstruction (sese.005) message. In this scenario, the transfer agent is FUNBGB22.

**P5126** The reference assigned to the original TransferInInstruction (sese.005) and for which the TransferInCancellationRequest sese.006 message is sent is PEFI-TI-002 and this is specified in the TransferReference element.

**P5127** XML Instance

**P5128** <TrfInCxlReq>

**P5129** 		<MsgId>

**P5130** 			<Id>IP2-0034</Id>

**P5131** 			<CreDtTm>2026-03-07T10:35:00</CreDtTm>

**P5132** 		</MsgId>

**P5133** 		<TrfRefs>

**P5134** 			<TrfRef>PEFI-TI-002</TrfRef>

**P5135** 		</TrfRefs>

**P5136** </TrfInCxlReq>

