---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order Status", "OrderInstructionStatusReport setr.016.001.05 – 1 Rejected"]
content_origin: "source-transcription"
---

# OrderInstructionStatusReport setr.016.001.05 – 1 Rejected

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Order Status / OrderInstructionStatusReport setr.016.001.05 – 1 Rejected.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3726** OrderInstructionStatusReport setr.016.001.05 – 1 Rejected

**P3727** Description

**P3728** An OrderInstructionStatusReport message is sent to report on the status of two orders. It reports the rejection of two individual orders that were previously instructed for account 44444444. The reasons for the rejections are given with a textual descriptions (rather than with codes).

**P3729** Order 1

**P3730** The individual order with reference Order 1 is rejected because the identification of the security is not recognised or is invalid.

**P3731** Order 2

**P3732** The individual order with reference Order 2 is rejected because there is not enough cash in the account to process the instruction.

**P3733** Message Instance

**P3734** <OrdrInstrStsRpt>

**P3735** 	<MsgId>

**P3736** 		<Id>O0001</Id>

**P3737** 		<CreDtTm>2026-01-08T09:30:30</CreDtTm>

**P3738** 	</MsgId>

**P3739** 	<StsRpt>

**P3740** 		<IndvOrdrDtlsRpt>

**P3741** 			<OrdrRef>Order 1</OrdrRef>

**P3742** 			<OrdrSts>

**P3743** 				<Rjctd>

**P3744** 					<AddtlInf>Financial Instrument ID not known</AddtlInf>

**P3745** 				</Rjctd>

**P3746** 			</OrdrSts>

**P3747** 		</IndvOrdrDtlsRpt>

**P3748** 		<IndvOrdrDtlsRpt>

**P3749** 			<OrdrRef>Order 2</OrdrRef>

**P3750** 			<OrdrSts>

**P3751** 				<Rjctd>

**P3752** 					<AddtlInf>Not enough cash</AddtlInf>

**P3753** 				</Rjctd>

**P3754** 			</OrdrSts>

**P3755** 		</IndvOrdrDtlsRpt>

**P3756** 	</StsRpt>

**P3757** </OrdrInstrStsRpt>

