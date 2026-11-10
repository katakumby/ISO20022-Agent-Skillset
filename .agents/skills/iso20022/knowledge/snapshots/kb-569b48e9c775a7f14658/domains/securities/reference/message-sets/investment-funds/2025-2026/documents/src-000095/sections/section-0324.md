---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Price Report", "PriceReport reda.001.001.05 – 1"]
content_origin: "source-transcription"
---

# PriceReport reda.001.001.05 – 1

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Price Report / PriceReport reda.001.001.05 – 1.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P5246** PriceReport reda.001.001.05 – 1

**P5247** Description

**P5248** A PriceReport message, is sent for two financial instruments. The price report, identification PriceReport001, is a ‘new’ price report (code NEWP, rather than a replacement or a partial correction). The price report contains two valuations:

**P5249** Valuation 1

**P5250** ISIN LU1234567890

**P5251** For trade date is 6 May 2013, the type of price is a net asset value, its exact value is EUR 1,000. 

**P5252** Valuation 2

**P5253** ISIN LU0987654321

**P5254** For trade date is 6 May 2026, the type of price is a net asset value, its exact value is EUR 1,010. 

**P5255** For both valuations, the valuation is official, not suspended, and the valuation timing is usual, as per the prospectus. The fund has only one price, which is cum dividend and can be used for execution.

**P5256** There is only one page for this message.

**P5257** Message Instance

**P5258** <PricRpt>

**P5259** 	<MsgId>

**P5260** 		<Id>0001</Id>

**P5261** 		<CreDtTm>2013-05-06T09:30:30</CreDtTm>

**P5262** 	</MsgId>

**P5263** 	<MsgPgntn>

**P5264** 		<PgNb>1</PgNb>

**P5265** 		<LastPgInd>true</LastPgInd>

**P5266** 	</MsgPgntn>

**P5267** 	<PricRptId>PriceReport001</PricRptId>

**P5268** 	<Fctn>NEWP</Fctn>

**P5269** 	<PricValtnDtls>

**P5270** 		<NAVDtTm>

**P5271** 		<Dt>2026-05-06</Dt>

**P5272** 		</NAVDtTm>

**P5273** 		<FinInstrmDtls>

**P5274** 			<Id>

**P5275** 				<ISIN>LU1234567890</ISIN>

**P5276** 			</Id>

**P5277** 			<DualFndInd>false</DualFndInd>

**P5278** 		</FinInstrmDtls>

**P5279** 		<ValtnTp>USUA</ValtnTp>

**P5280** 		<OffclValtnInd>true</OffclValtnInd>

**P5281** 		<SspdInd>false</SspdInd>

**P5282** 		<PricDtls>

**P5283** 			<Tp>

**P5284** 				<Cd>NAVL</Cd>

**P5285** 			</Tp>

**P5286** 			<ValInInvstmtCcy>

**P5287** 				<Amt Ccy="EUR">1000</Amt>

**P5288** 			</ValInInvstmtCcy>

**P5289** 			<ForExctnInd>true</ForExctnInd>

**P5290** 			<CumDvddInd>true</CumDvddInd>

**P5291** 			<EstmtdPricInd>false</EstmtdPricInd>

**P5292** 		</PricDtls>

**P5293** 	</PricValtnDtls>

**P5294** 	<PricValtnDtls>

**P5295** 		<NAVDtTm>

**P5296** 			<Dt>2026-05-06</Dt>

**P5297** 		</NAVDtTm>

**P5298** 		<FinInstrmDtls>

**P5299** 			<Id>

**P5300** 				<ISIN>LU0987654321</ISIN>

**P5301** 			</Id>

**P5302** 			<DualFndInd>false</DualFndInd>

**P5303** 		</FinInstrmDtls>

**P5304** 		<ValtnTp>USUA</ValtnTp>

**P5305** 		<OffclValtnInd>true</OffclValtnInd>

**P5306** 		<SspdInd>false</SspdInd>

**P5307** 		<PricDtls>

**P5308** 			<Tp>

**P5309** 				<Cd>NAVL</Cd>

**P5310** 			</Tp>

**P5311** 			<ValInInvstmtCcy>

**P5312** 				<Amt Ccy="EUR">1010</Amt>

**P5313** 			</ValInInvstmtCcy>

**P5314** 			<ForExctnInd>true</ForExctnInd>

**P5315** 			<CumDvddInd>true</CumDvddInd>

**P5316** 			<EstmtdPricInd>false</EstmtdPricInd>

**P5317** 		</PricDtls>

**P5318** 	</PricValtnDtls>

**P5319** </PricRpt>

