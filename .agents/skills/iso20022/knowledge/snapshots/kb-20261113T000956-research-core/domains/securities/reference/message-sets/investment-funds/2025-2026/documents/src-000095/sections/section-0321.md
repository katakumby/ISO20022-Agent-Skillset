---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Transfer Reversal", "ReversalOfTransferOutConfirmation sese.004.001.09"]
content_origin: "source-transcription"
---

# ReversalOfTransferOutConfirmation sese.004.001.09

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Transfer Reversal / ReversalOfTransferOutConfirmation sese.004.001.09.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P5185** ReversalOfTransferOutConfirmation sese.004.001.09

**P5186** Description

**P5187** A ReversalOfTransferOutConfirmation is sent by an executing party, such as a transfer agent, to the instructing party, such as the old plan manager (transferor), to reverse a previously sent transfer out confirmation.

**P5188** The reference assigned to the original TransferOutInstruction (sese.001) message and subsequently echoed back in the TransferOutConfirmation (sese.003) message, is specified in the TransferReference element.

**P5189** The CounterpartyReference of the original TransferOutInstruction (sese.001) message, if provided, and subsequently echoed back in the TransferOutConfirmation (sese.003) message, may also be quoted.

**P5190** The executing party's reference, as assigned to the original TransferOutConfirmation (sese.003) message, may also be quoted in the TransferConfirmationReference element.

**P5191** In this scenario: 

**P5192** the reference assigned in the original TransferOutInstruction (sese.001) message is BDAP-TO-001

**P5193** the CounterpartyReference of the original TransferOutInstruction (sese.001) message is PEFI-TI-U001 and the reference issuer is PEFIGB22

**P5194** the executing party's reference assigned to the original TransferOutConfirmation (sese.003) message is TATA-001

**P5195** XML Instance

**P5196** <RvslOfTrfOutConf>

**P5197** 		<MsgId>

**P5198** 			<Id>34-0017</Id>

**P5199** 			<CreDtTm>2026-03-08T14:25:00</CreDtTm>

**P5200** 		</MsgId>

**P5201** 		<RvslRefs>

**P5202** 			<TrfRef>BDAP-TO-001</TrfRef>

**P5203** 			<TrfConfRef>TATA-001</TrfConfRef>

**P5204** 			<CtrPtyRef>

**P5205** 				<Ref>PEFI-TI-U001</Ref>

**P5206** 				<RefIssr>

**P5207** 					<Pty>

**P5208** 						<AnyBIC>PEFILULL</AnyBIC>

**P5209** 					</Pty>

**P5210** 				</RefIssr>

**P5211** 			</CtrPtyRef>

**P5212** 		</RvslRefs>

**P5213** 	</RvslOfTrfOutConf>

