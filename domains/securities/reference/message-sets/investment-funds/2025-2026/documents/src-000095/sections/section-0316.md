---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Transfer Cancellation", "TransferOutCancellationRequest sese.002.001.09"]
content_origin: "source-transcription"
---

# TransferOutCancellationRequest sese.002.001.09

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Transfer Cancellation / TransferOutCancellationRequest sese.002.001.09.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P5097** TransferOutCancellationRequest sese.002.001.09

**P5098** Description

**P5099** A TransferOutCancellationRequest is sent by the old plan manager (transferor), BDAPGB2, to the executing party, the transfer agent to request the cancellation of a previously sent TransferOutInstruction message. In this scenario, the transfer agent is TATAGB22.

**P5100** The reference assigned to the original TransferOutInstruction (sese.001) message and for which the TransferOutCancellationRequest (sese.002) message is sent is BDAP-TO-001 and this is specified in the TransferReference element.

**P5101** Other References

**P5102** The CounterpartyReference of the original TransferOutInstruction (sese.001), if provided, may also be quoted. The reference specified was PEFI-TI-U001 and the reference issuer was PEFIGB22

**P5103** The reference that was assigned to the transfer of the portfolio as a whole and specified in the MasterReference element in the original TransferOutInstruction (sese.001) message, if provided, may also be specified. The reference specified was PORT-GB-001.

**P5104** XML Instance

**P5105** <TrfOutCxlReq>

**P5106** 		<MsgId>

**P5107** 			<Id>IP1-0012</Id>

**P5108** 			<CreDtTm>2026-03-07T10:25:00</CreDtTm>

**P5109** 		</MsgId>

**P5110** 		<MstrRef>PORT-GB-001</MstrRef>

**P5111** 		<TrfRefs>

**P5112** 			<TrfRef>BDAP-TO-001</TrfRef>

**P5113** 			<CtrPtyRef>

**P5114** 				<Ref>PEFI-TI-U001</Ref>

**P5115** 				<RefIssr>

**P5116** 					<Pty>

**P5117** 						<AnyBIC>PEFIGB22</AnyBIC>

**P5118** 					</Pty>

**P5119** 				</RefIssr>

**P5120** 			</CtrPtyRef>

**P5121** 		</TrfRefs>

**P5122** </TrfOutCxlReq>

