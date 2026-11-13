---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Transfer - Single Leg Transfer (SLT) ", "TransferOutConfirmation sese.003.001.10"]
content_origin: "source-transcription"
---

# TransferOutConfirmation sese.003.001.10

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Transfer - Single Leg Transfer (SLT)  / TransferOutConfirmation sese.003.001.10.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4750** TransferOutConfirmation sese.003.001.10

**P4751** Description

**P4752** A TransferOutConfirmation message is sent by the executing party, which, in this scenario, is the transfer agent, to the instructing party, the transferor (old plan manager). The transfer agent confirms that 2,000 units of the fund ISIN GB1111111111, Ethical Green Fund, have been transferred into the account of PEFIGB22 (transferee), account 444444. The units were transferred from the account of BDAPGB22 (transferor), account 999999.

**P4753** All references are echoed back.

**P4754** The transfer agent assigns the reference TATA-001 to the confirmation.

**P4755** XML Instance

**P4756** <TrfOutConf>

**P4757** 		<MsgId>

**P4758** 			<Id>34-0001</Id>

**P4759** 			<CreDtTm>2026-03-08T14:15:00</CreDtTm>

**P4760** 		</MsgId>

**P4761** 		<MstrRef>PORT-GB-001</MstrRef>

**P4762** 		<TrfDtls>

**P4763** 			<TrfConfRef>TATA-001</TrfConfRef>

**P4764** 			<TrfRef>BDAP-TO-001</TrfRef>

**P4765** 			<CtrPtyRef>

**P4766** 				<Ref>PEFI-TI-U001</Ref>

**P4767** 				<RefIssr>

**P4768** 					<Pty>

**P4769** 						<AnyBIC>PEFIGB22</AnyBIC>

**P4770** 					</Pty>

**P4771** 			</CtrPtyRef>

**P4772** 			<BizFlowTp>SLDP</BizFlowTp>

**P4773** 			<FctvTrfDt>

**P4774** 				<Dt>2026-03-08</Dt>

**P4775** 			</FctvTrfDt>

**P4776** 			<FinInstrmDtls>

**P4777** 					<Id>

**P4778** 					<ISIN>GB1111111111</ISIN>

**P4779** 				</Id>

**P4780** 				<Nm>Ethical Green Fund </Nm>

**P4781** 			</FinInstrmDtls>

**P4782** 			<TtlUnitsNb>2000</TtlUnitsNb>

**P4783** 		</TrfDtls>

**P4784** 		<AcctDtls>

**P4785** 			<AcctId>999999</AcctId>

**P4786** 		</AcctDtls>

**P4787** 		<SttlmDtls>

**P4788** 			<Trfee>

**P4789** 				<Pty>

**P4790** 				<AnyBIC>PEFIGB22</AnyBIC>

**P4791** 				</Pty>

**P4792** 			</Trfee>

**P4793** 			<TrfeeRegdAcct>

**P4794** 				<Id>444444</Id>

**P4795** 			</TrfeeRegdAcct>

**P4796** 		</SttlmDtls>

**P4797** </TrfOutConf>

