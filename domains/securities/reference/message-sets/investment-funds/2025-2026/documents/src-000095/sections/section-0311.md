---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Transfer - Matched Leg Transfer (MLT)", "TransferInConfirmation sese.007.001.10"]
content_origin: "source-transcription"
---

# TransferInConfirmation sese.007.001.10

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Transfer - Matched Leg Transfer (MLT) / TransferInConfirmation sese.007.001.10.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4982** TransferInConfirmation sese.007.001.10

**P4983** Description

**P4984** A TransferInConfirmation message is sent by the executing party, which, in this scenario is the transfer agent, to the instructing party, the transferee (new plan manager). In this scenario, the executing party is the transfer agent FUNBGB22. The transfer agent confirms that 300 units of the fund ISIN GB4444444444, Ethical Blue Fund, have been transferred into the account of PEFIGB22 (transferee), account 555555. The units were transferred from the account of BDAPGB22 (transferor), account 888888. 

**P4985** All references in the TransferInInstruction sese.005 are echoed back.

**P4986** The transfer agent assigns the reference FUNB-022 to the transfer in confirmation.

**P4987** Message Instance

**P4988** <TrfInConf>

**P4989** 		<MsgId>

**P4990** 			<Id>34-0054</Id>

**P4991** 			<CreDtTm>2026-03-08T14:15:00</CreDtTm>

**P4992** 		</MsgId>

**P4993** 		<TrfDtls>

**P4994** 			<TrfConfRef>FUNB-022</TrfConfRef>

**P4995** 			<TrfRef>PEFI-TO-002 </TrfRef>

**P4996** 			<BizFlowTp>DLPR</BizFlowTp>

**P4997** 			<FctvTrfDt>

**P4998** 				<Dt>2026-03-08</Dt>

**P4999** 			</FctvTrfDt>

**P5000** 			<FinInstrmDtls>

**P5001** 				<Id>

**P5002** 					<ISIN>GB4444444444</ISIN>

**P5003** 				</Id>

**P5004** 				<Nm>Ethical Blue Fund </Nm>

**P5005** 			</FinInstrmDtls>

**P5006** 			<TtlUnitsNb>3000</TtlUnitsNb>

**P5007** 		</TrfDtls>

**P5008** 		<AcctDtls>

**P5009** 			<AcctId>555555</AcctId>

**P5010** 		</AcctDtls>

**P5011** 		<SttlmDtls>

**P5012** 			<Trfr>

**P5013** 				<Pty>

**P5014** 					<AnyBIC>BDAPGB22</AnyBIC>

**P5015** 				</Pty>

**P5016** 			</Trfr>

**P5017** 			<TrfrRegdAcct>

**P5018** 				<Id>88888888</Id>

**P5019** 				<Svcr>

**P5020** 					<Pty>

**P5021** 						<AnyBIC>FUNBGB22</AnyBIC>

**P5022** 					</Pty>

**P5023** 				</Svcr>

**P5024** 			</TrfrRegdAcct>

**P5025** 		</SttlmDtls>

**P5026** </TrfInConf>

