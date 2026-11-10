---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order Status", "OrderInstructionStatusReport setr.016.001.05 – 4 Gated Redemption "]
content_origin: "source-transcription"
---

# OrderInstructionStatusReport setr.016.001.05 – 4 Gated Redemption 

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Order Status / OrderInstructionStatusReport setr.016.001.05 – 4 Gated Redemption .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3809** OrderInstructionStatusReport setr.016.001.05 – 4 Gated Redemption 

**P3810** Description

**P3811** An OrderInstructionStatusReport message is sent to report on the status of a redemption order. It reports that an order, with order reference Order 22, is partially settled, the redemption has been gated and all settlement will be done at the same price (GAT1).

**P3812** Message Instance

**P3813** <OrdrInstrStsRpt>

**P3814** 	<MsgId>

**P3815** 		<Id>O0001</Id>

**P3816** 		<CreDtTm>2026-01-08T09:30:30</CreDtTm>

**P3817** 	</MsgId>

**P3818** 	<StsRpt>

**P3819** 		<IndvOrdrDtlsRpt>

**P3820** 			<OrdrRef>Order 22</OrdrRef>

**P3821** 			<OrdrSts>

**P3822** 				<PrtlySttld>

**P3823** 					<Rsn>

**P3824** 						<Cd>GAT1</Cd>

**P3825** 					</Rsn>

**P3826** 				</PrtlySttld>

**P3827** 			</OrdrSts>

**P3828** 		</IndvOrdrDtlsRpt>

**P3829** 	</StsRpt>

**P3830** </OrdrInstrStsRpt>

