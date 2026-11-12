---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Transfer Reversal", "ReversalOfTransferInConfirmation sese.008.001.09"]
content_origin: "source-transcription"
---

# ReversalOfTransferInConfirmation sese.008.001.09

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Transfer Reversal / ReversalOfTransferInConfirmation sese.008.001.09.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P5215** ReversalOfTransferInConfirmation sese.008.001.09

**P5216** Description

**P5217** A ReversalOfTransferInConfirmation is sent by an executing party, such as a transfer agent, to the instructing party, such as the new plan manager (transferee) or the transferee's custodian, to reverse a previously sent transfer in confirmation.

**P5218** In this scenario, the process was single leg transfer (SL) and so there was no TransferInInstruction (sese.005) message in the transaction chain. Therefore NONREF is quoted in the mandatory TransferReference element of the ReversalOfTransferInConfirmation (sese.008) message.

**P5219** The CounterpartyReference of the original TransferOutInstruction (sese.001) message, if provided, and subsequently passed forward in the TransferInConfirmation (sese.007) message as the ClientReference, may also be specified.

**P5220** The executing party's reference, as assigned to the original TransferInConfirmation (sese.007) message, may also be quoted in the TransferConfirmationReference element.

**P5221** In this scenario: 

**P5222** 'NONREF' is specified in the TransferReference element

**P5223** the ClientReference of the original TransferInConfirmation (sese.007) message is PEFI-TI-U001 and the reference issuer is PEFIGB22 

**P5224** the executing party's reference assigned to the original TransferInConfirmation (sese.007) message is TATA-002.

**P5225** XML Instance

**P5226** <RvslOfTrfInConf>

**P5227** 		<MsgId>

**P5228** 			<Id>34-0018</Id>

**P5229** 			<CreDtTm>2026-03-08T14:26:00</CreDtTm>

**P5230** 		</MsgId>

**P5231** 		<RvslRefs>

**P5232** 			<TrfRef>NONREF</TrfRef>

**P5233** 			<ClntRef>

**P5234** 				<Ref>PEFI-TI-U001 </Ref>

**P5235** 				<RefIssr>

**P5236** 					<Pty>

**P5237** 						<AnyBIC>PEFILULL</AnyBIC>

**P5238** 					</Pty>

**P5239** 				</RefIssr>

**P5240** 			</ClntRef>

**P5241** 			<TrfConfRef>TATA-002</TrfConfRef>

**P5242** 		</RvslRefs>

**P5243** 	</RvslOfTrfInConf>

