---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Transfer Status", "TransferInstructionStatusReport sese.011.001.10 – Rejected"]
content_origin: "source-transcription"
---

# TransferInstructionStatusReport sese.011.001.10 – Rejected

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Transfer Status / TransferInstructionStatusReport sese.011.001.10 – Rejected.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P5061** TransferInstructionStatusReport sese.011.001.10 – Rejected

**P5062** Description

**P5063** A TransferInstructionStatusReport message is sent by an executing party, such as a transfer agent, to the instructing party, such as the old plan manager (transferor) or the new plan manager (transferee) or a custodian in the transaction chain.

**P5064** In this scenario, the TransferInstructionStatusReport message is providing the status of a TransferOutInstruction (sese.001) message.

**P5065** The reference assigned to the original TransferOutInstruction (sese.001) message and for which the status is reported is BDAP-TO-001 and this is specified in the TransferReference element.

**P5066** Other References

**P5067** The CounterpartyReference of the original TransferOutInstruction (sese.001) message, if provided, may also be quoted. The reference specified was PEFI-TI-U001 and the reference issuer was PEFIGB22.

**P5068** The reference that was assigned to the transfer of the portfolio as a whole and specified in the MasterReference element in the original TransferOutInstruction (sese.001), if provided, may also be specified. The reference specified was PORT-GB-001.

**P5069** In this scenario, the TransferInstructionStatusReport message specifies that the status of the transfer instruction is rejected because the financial instrument is not recognised (reason code DSEC).

**P5070** XML Instance

**P5071** <TrfInstrStsRpt>

**P5072** 		<MsgId>

**P5073** 			<Id>34-0052</Id>

**P5074** 			<CreDtTm>2026-03-08T12:16:00</CreDtTm>

**P5075** 		</MsgId>

**P5076** 		<CtrPtyRef>

**P5077** 			<Ref>PEFI-TI-U001 </Ref>

**P5078** 			<RefIssr>

**P5079** 				<Pty>

**P5080** 					<AnyBIC>PEFIGB22</AnyBIC>

**P5081** 				</Pty>

**P5082** 			</RefIssr>

**P5083** 		</CtrPtyRef>

**P5084** 		<StsRpt>

**P5085** 		<MstrRef>PORT-GB-001</MstrRef>

**P5086** 			<TrfRef>BDAP-TO-001 </TrfRef>

**P5087** 			<TrfSts>

**P5088** 				<Rjctd>

**P5089** 					<Rsn>

**P5090** 						<Cd>DSEC</Cd>

**P5091** 					</Rsn>

**P5092** 				</Rjctd>

**P5093** 			</TrfSts>

**P5094** 		</StsRpt>

**P5095** 	</TrfInstrStsRpt>

