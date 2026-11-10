---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Transfer - Matched Leg Transfer (MLT)", "TransferOutConfirmation sese.003.001.10"]
content_origin: "source-transcription"
---

# TransferOutConfirmation sese.003.001.10

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Transfer - Matched Leg Transfer (MLT) / TransferOutConfirmation sese.003.001.10.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4894** TransferOutConfirmation sese.003.001.10

**P4895** Description

**P4896** A TransferOutConfirmation message is sent by the executing party, which, in this scenario is the transfer agent, to the instructing party, the transferor (old plan manager). In this scenario, the executing party is the transfer agent FUNBGB22. The transfer agent confirms that 300 units of the fund ISIN GB4444444444, Ethical Blue Fund, have been transferred into the account of PEFIGB22 (transferee), account 555555. The units were transferred from the account of BDAPGB22 (transferor), account 888888.

**P4897** All references in the TransferOutInstruction (sese.001) message are echoed back.

**P4898** The transfer agent assigns the reference FUNB-021 to the transfer out confirmation.

**P4899** XML Instance 

**P4900** <TrfOutConf>

**P4901** 		<MsgId>

**P4902** 			<Id>34-0053</Id>

**P4903** 			<CreDtTm>2026-03-08T14:15:00</CreDtTm>

**P4904** 		</MsgId>

**P4905** 		<TrfDtls>

**P4906** 			<TrfConfRef>FUNB-021</TrfConfRef>

**P4907** 			<TrfRef>BDAP-TO-001</TrfRef>

**P4908** 			<BizFlowTp>DLPR</BizFlowTp>

**P4909** 			<FctvTrfDt>

**P4910** 				<Dt>2026-03-08</Dt>

**P4911** 			</FctvTrfDt>

**P4912** 			<FinInstrmDtls>

**P4913** 				<Id>

**P4914** 					<ISIN>GB4444444444</ISIN>

**P4915** 				</Id>

**P4916** 				<Nm>Ethical Blue Fund </Nm>

**P4917** 			</FinInstrmDtls>

**P4918** 			<TtlUnitsNb>300</TtlUnitsNb>

**P4919** 		</TrfDtls>

**P4920** 		<AcctDtls>

**P4921** 			<AcctId>888888</AcctId>

**P4922** 		</AcctDtls>

**P4923** 		<SttlmDtls>

**P4924** 			<Trfee>

**P4925** 				<Pty>

**P4926** 				<AnyBIC>PEFIGB22</AnyBIC>

**P4927** 				</Pty>

**P4928** 			</Trfee>

**P4929** 			<TrfeeRegdAcct>

**P4930** 				<Id>555555</Id>

**P4931** 				<Svcr>

**P4932** 					<Pty>

**P4933** 						<AnyBIC>FUNBGB22</AnyBIC>

**P4934** 					</Pty>

**P4935** 				</Svcr>

**P4936** 			</TrfeeRegdAcct>

**P4937** 		</SttlmDtls>

**P4938** </TrfOutConf>

