---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Price Report", "PriceReport reda.001.001.05 – 1", "PriceReport reda.001.001.05 - 2"]
content_origin: "source-transcription"
---

# PriceReport reda.001.001.05 - 2

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Price Report / PriceReport reda.001.001.05 – 1 / PriceReport reda.001.001.05 - 2.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P5320** PriceReport reda.001.001.05 - 2

**P5321** Description

**P5322** A PriceReport message is sent as a price report correction. The price report, identification PriceReport001, is a sent to provide corrected prices for two financial instruments, the message is a ‘complete replacement of a price report’ (code REPL). The price report contains two corrected valuations:

**P5323** Valuation 1 

**P5324** Correction: ISIN LU1234567890

**P5325** For trade date is 6 May 2026, the type of price is a net asset value, its exact value is EUR 1,020. 

**P5326** Valuation 2 

**P5327** Correction: ISIN LU0987654321

**P5328** For trade date is 6 May 2026, the type of price is a net asset value, its exact value is EUR 1,030. 

**P5329** For both valuations, the valuation is official, not suspended, and the valuation timing is usual, as per the prospectus. The fund has only one price, which is cum dividend and can be used for execution.

**P5330** There is only one page for this message.

**P5331** Message Instance

**P5332** <PricRpt>

**P5333** 		<MsgId>

**P5334** 			<Id>0005</Id>

**P5335** 			<CreDtTm>2026-05-06T09:40:30</CreDtTm>

**P5336** 		</MsgId>

**P5337** 		<MsgPgntn>

**P5338** 			<PgNb>1</PgNb>

**P5339** 			<LastPgInd>true</LastPgInd>

**P5340** 		</MsgPgntn>

**P5341** 		<PricRptId>PriceReport001</PricRptId>

**P5342** 		<Fctn>REPL</Fctn>

**P5343** 		<PricValtnDtls>

**P5344** 			<NAVDtTm>

**P5345** 				<Dt>2026-05-06</Dt>

**P5346** 			</NAVDtTm>

**P5347** 			<FinInstrmDtls>

**P5348** 				<Id>

**P5349** 					<ISIN>LU1234567890</ISIN>

**P5350** 				</Id>

**P5351** 				<DualFndInd>false</DualFndInd>

**P5352** 			</FinInstrmDtls>

**P5353** 			<ValtnTp>USUA</ValtnTp>

**P5354** 			<OffclValtnInd>true</OffclValtnInd>

**P5355** 			<SspdInd>false</SspdInd>

**P5356** 			<PricDtls>

**P5357** 				<Tp>

**P5358** 					<Cd>NAVL</Cd>

**P5359** 				</Tp>

**P5360** 				<ValInInvstmtCcy>

**P5361** 					<Amt Ccy="EUR">1000</Amt>

**P5362** 				</ValInInvstmtCcy>

**P5363** 				<ForExctnInd>true</ForExctnInd>

**P5364** 				<CumDvddInd>true</CumDvddInd>

**P5365** 				<EstmtdPricInd>false</EstmtdPricInd>

**P5366** 			</PricDtls>

**P5367** 		</PricValtnDtls>

**P5368** 		<PricValtnDtls>

**P5369** 			<NAVDtTm>

**P5370** 				<Dt>2026-05-06</Dt>

**P5371** 			</NAVDtTm>

**P5372** 			<FinInstrmDtls>

**P5373** 				<Id>

**P5374** 					<ISIN>LU0987654321</ISIN>

**P5375** 				</Id>

**P5376** 				<DualFndInd>false</DualFndInd>

**P5377** 			</FinInstrmDtls>

**P5378** 			<ValtnTp>USUA</ValtnTp>

**P5379** 			<OffclValtnInd>true</OffclValtnInd>

**P5380** 			<SspdInd>false</SspdInd>

**P5381** 			<PricDtls>

**P5382** 				<Tp>

**P5383** 					<Cd>NAVL</Cd>

**P5384** 				</Tp>

**P5385** 				<ValInInvstmtCcy>

**P5386** 					<Amt Ccy="EUR">1010</Amt>

**P5387** 				</ValInInvstmtCcy>

**P5388** 				<ForExctnInd>true</ForExctnInd>

**P5389** 				<CumDvddInd>true</CumDvddInd>

**P5390** 				<EstmtdPricInd>false</EstmtdPricInd>

**P5391** 			</PricDtls>

**P5392** 		</PricValtnDtls>

**P5393** </PricRpt>

