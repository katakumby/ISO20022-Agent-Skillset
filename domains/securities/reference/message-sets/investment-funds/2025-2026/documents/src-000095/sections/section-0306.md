---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Transfer - Single Leg Transfer (SLT) ", "TransferInConfirmation sese.007.001.10"]
content_origin: "source-transcription"
---

# TransferInConfirmation sese.007.001.10

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Transfer - Single Leg Transfer (SLT)  / TransferInConfirmation sese.007.001.10.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4798** TransferInConfirmation sese.007.001.10

**P4799** Description

**P4800** A TransferInConfirmation message is sent by the executing party, which, in this scenario, is the transfer agent, to the transferee (new plan manager). The transfer agent confirms that 2,000 units of the fund ISIN GB1111111111, Ethical Green Fund, have been transferred into the account of PEFIGB22 (transferee), account 444444. The units were transferred from the account of BDAPGB22 (transferor), account 999999.

**P4801** The MasterReference element and the transferee's reference for the transfer of the individual asset, as specified in the CounterpartyReference element in the TransferOutInstruction (sese.001) message received by the transfer agent, are passed through into the TransferInConfirmation (sese.007) message. 

**P4802** In the TransferInConfirmation message, the transferee's reference for the transfer of the individual asset is specified in the ClientReference sequence.

**P4803** As this TransferInConfirmation is not being sent in response to a TransferInInstruction (sese.005) message, the TransferReference element in the TransferInConfirmation contains the value NONREF. 

**P4804** The transfer agent assigns the reference TATA-002 to the confirmation.

**P4805** XML Instance

**P4806** <TrfInConf>

**P4807** 		<MsgId>

**P4808** 			<Id>34-0002</Id>

**P4809** 			<CreDtTm>2026-03-08T14:16:00</CreDtTm>

**P4810** 		</MsgId>

**P4811** 		<MstrRef>PORT-GB-001</MstrRef>

**P4812** 		<TrfDtls>

**P4813** 			<TrfConfRef>TATA-002</TrfConfRef>

**P4814** 			<TrfRef>NONREF </TrfRef>

**P4815** 			<ClntRef>

**P4816** 				<Ref>PEFI-TI-U001</Ref>

**P4817** 				<RefIssr>

**P4818** 					<Pty>

**P4819** 						<AnyBIC>PEFIGB22</AnyBIC>

**P4820** 					<Pty>

**P4821** 				</RefIssr>

**P4822** 			</ClntRef>

**P4823** 			<BizFlowTp>SLDP</BizFlowTp>

**P4824** 			<FctvTrfDt>

**P4825** 				<Dt>2026-03-08</Dt>

**P4826** 			</FctvTrfDt>

**P4827** 			<FinInstrmDtls>

**P4828** 					<Id>

**P4829** 					<ISIN>GB1111111111</ISIN>

**P4830** 				</Id>

**P4831** 				<Nm>Ethical Green Fund </Nm>

**P4832** 			</FinInstrmDtls>

**P4833** 			<TtlUnitsNb>2000</TtlUnitsNb>

**P4834** 		</TrfDtls>

**P4835** 		<AcctDtls>

**P4836** 			<AcctId>444444</AcctId>

**P4837** 		</AcctDtls>

**P4838** 		<SttlmDtls>

**P4839** 			<Trfr>

**P4840** 				<Pty>

**P4841** 					<AnyBIC>BDAPGB22</AnyBIC>

**P4842** 				</Pty>

**P4843** 			</Trfr>

**P4844** 			<TrfrRegdAcct>

**P4845** 				<Id>999999</Id>

**P4846** 			</TrfrRegdAcct>

**P4847** 		</SttlmDtls>

**P4848** </TrfInConf>

