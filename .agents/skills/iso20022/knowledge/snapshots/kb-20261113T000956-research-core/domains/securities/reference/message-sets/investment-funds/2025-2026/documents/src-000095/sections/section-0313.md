---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Transfer Status", "TransferInstructionStatusReport sese.011.001.10 – Accepted (PACK)"]
content_origin: "source-transcription"
---

# TransferInstructionStatusReport sese.011.001.10 – Accepted (PACK)

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Transfer Status / TransferInstructionStatusReport sese.011.001.10 – Accepted (PACK).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P5028** TransferInstructionStatusReport sese.011.001.10 – Accepted (PACK)

**P5029** Description

**P5030** A TransferInstructionStatusReport message is sent by an executing party, such as a transfer agent, to the instructing party, such as the old plan manager (transferor) or the new plan manager (transferee) or a custodian in the transaction chain.

**P5031** In this scenario, the TransferInstructionStatusReport message is providing the status of a TransferOutInstruction (sese.001) message.

**P5032** The reference assigned to the original TransferOutInstruction (sese.001) message and, for which the status is reported, is BDAP-TO-001 and this is specified in the TransferReference element.

**P5033** Other References

**P5034** The CounterpartyReference of the original TransferOutInstruction (sese.001) message, if provided, may also be quoted. The reference specified was PEFI-TI-U001 and the reference issuer was PEFIGB22.

**P5035** The reference that was assigned to the transfer of the portfolio as a whole and specified in the MasterReference element in the original TransferOutInstruction (sese.001) message, if provided, may also be specified. The reference specified was PORT-GB-001

**P5036** In this scenario, the TransferInstructionStatusReport message specifies that the status of the transfer instruction has been accepted for further processing (status PACK).

**P5037** XML Instance

**P5038** <TrfInstrStsRpt>

**P5039** 		<MsgId>

**P5040** 			<Id>34-0052</Id>

**P5041** 			<CreDtTm>2026-03-08T12:15:00</CreDtTm>

**P5042** 		</MsgId>

**P5043** 		<CtrPtyRef>

**P5044** 			<Ref>PEFI-TI-U001 </Ref>

**P5045** 			<RefIssr>

**P5046** 				<Pty>

**P5047** 					<AnyBIC>PEFIGB22</AnyBIC>

**P5048** 				</Pty>

**P5049** 			</RefIssr>

**P5050** 		</CtrPtyRef>

**P5051** 		<StsRpt>

**P5052** 		<MstrRef>PORT-GB-001</MstrRef>

**P5053** 			<TrfRef>BDAP-TO-001 </TrfRef>

**P5054** 			<TrfSts>

**P5055** 				<Sts>

**P5056** 					<Sts>PACK</Sts>

**P5057** 				</Sts>

**P5058** 			</TrfSts>

**P5059** 		</StsRpt>

**P5060** </TrfInstrStsRpt>

