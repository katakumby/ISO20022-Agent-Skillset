---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Transfer Cancellation", "TransferCancellationStatusReport sese.010.001.07"]
content_origin: "source-transcription"
---

# TransferCancellationStatusReport sese.010.001.07

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Transfer Cancellation / TransferCancellationStatusReport sese.010.001.07.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P5137** TransferCancellationStatusReport sese.010.001.07

**P5138** Description

**P5139** A TransferCancellationStatusReport message is sent by an executing party to the instructing party in response to a TransferOutCancellationRequest (sese.002) or TransferInCancellationRequest (sese.006) message. In this scenario, the TransferCancellationStatusReport (sese.010) message is sent in response to a TransferOutCancellationRequest (sese.002) message.

**P5140** The reference assigned to the original TransferOutInstruction (sese.001) message and subsequently quoted in the TransferOutCancellationRequest (sese.002) message, is BDAP-TO-001 and this specified in the TransferReference element.

**P5141** Other References

**P5142** The CounterpartyReference of the original TransferOutInstruction (sese.001), if provided, may also be quoted. The reference specified was PEFI-TI-U001 and the reference issuer was PEFIGB22

**P5143** The reference that was assigned to the transfer of the portfolio as a whole and specified in the MasterReference element in the original TransferOutInstruction (sese.001) message, if provided, may also be specified. The reference specified was PORT-GB-001.

**P5144** In this scenario, the TransferCancellationStatusReport (sese.010) reports that the cancellation request is rejected because it was sent after the cut-off time (rejected reason CUTO).

**P5145** XML Instance

**P5146** <TrfCxlStsRpt>

**P5147** 		<MsgId>

**P5148** 			<Id>34-0062</Id>

**P5149** 			<CreDtTm>2026-03-07T10:55:00</CreDtTm>

**P5150** 		</MsgId>

**P5151** 		<CtrPtyRef>

**P5152** 			<Ref>PEFI-TI-U001 </Ref>

**P5153** 			<RefIssr>

**P5154** 				<Pty>

**P5155** 					<AnyBIC>PEFIGB22</AnyBIC>

**P5156** 				</Pty>

**P5157** 			</RefIssr>

**P5158** 		</CtrPtyRef>

**P5159** 		<StsRpt>

**P5160** 			<MstrRef>PORT-GB-001</MstrRef>

**P5161** 			<TrfRef>BDAP-TO-001</TrfRef>

**P5162** 			<Sts>

**P5163** 				<Rjctd>

**P5164** 					<Rsn>

**P5165** 						<Cd>CUTO</Cd>

**P5166** 					</Rsn>

**P5167** 				</Rjctd>

**P5168** 			</Sts>

**P5169** 		</StsRpt>

**P5170** </TrfCxlStsRpt>

