---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_ids: []
heading_path: ["Business Examples", "Security Creation Request - reda.006.001.01"]
content_origin: "source-transcription"
---

# Security Creation Request - reda.006.001.01

Source: [src-000377](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Locator: heading path Business Examples / Security Creation Request - reda.006.001.01.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P320** Security Creation Request - reda.006.001.01

**P321** Description

**P322** The instructing Party wants to create a new security with the following information:

**P323** ISIN: SECXXXYYYZZ1

**P324** Security Long Name: Sample equity shares, Fixed Interest Rate

**P325** Security Short Name: Sample ES, FIR

**P326** Valid From Name: 2020-01-01

**P327** Denomination Currency: EUR

**P328** Expiry Date: 2030-12-31

**P329** Classification Type: ESFUFR

**P330** Country of Issue: IT

**P331** Issue Date: 2020-01-01

**P332** ISIN Valid From: 2020-01-01

**P333** Quantity Type: UNIT

**P334** Minimum Denomination: 100

**P335** Minimum Multiple Quantity: 10

**P336** Deviating Settlement Unit: 60,67

**P337** Message Instance

**P338** <Document>

**P339** 	<SctyCreReq>

**P340** 		<MsgHdr>

**P341** 			<MsgId>SAMPLECRESEC001</MsgId>

**P342** 		</MsgHdr>

**P343** 		<Scty>

**P344** 			<FinInstrmId>

**P345** 				<ISIN>SECXXXYYYZZ1</ISIN>

**P346** 			</FinInstrmId>

**P347** 			<FinInstrmAttrbts>

**P348** 				<ISOSctyLngNm>Sample equity shares, Fixed Interest Rate</ISOSctyLngNm>

**P349** 				<ISOSctyShrtNm>Sample ES, FIR</ISOSctyShrtNm>

**P350** 				<NmVldFr>

**P351** 					<Dt>2020-01-01</Dt>

**P352** 				</NmVldFr>

**P353** 				<DnmtnCcy>EUR</DnmtnCcy>

**P354** 				<XpryDt>2030-12-31</XpryDt>

**P355** 				<ClssfctnTp>

**P356** 					<ClssfctnFinInstrm>ESXXXX</ClssfctnFinInstrm>

**P357** 				</ClssfctnTp>

**P358** 				<Issnc>

**P359** 					<CtryOfIsse>IT</CtryOfIsse>

**P360** 					<IsseDt>2020-01-01</IsseDt>

**P361** 					<ISINVldFr>2020-01-01</ISINVldFr>

**P362** 				</Issnc>

**P363** 				<SttlmInf>

**P364** 					<SctiesQtyTp>

**P365** 						<Cd>UNIT</Cd>

**P366** 					</SctiesQtyTp>

**P367** 					<MinDnmtn>

**P368** 						<Unit>100</Unit>

**P369** 					</MinDnmtn>

**P370** 					<MinMltplQty>

**P371** 						<Unit>10</Unit>

**P372** 					</MinMltplQty>

**P373** 					<DevtgSttlmUnit>

**P374** 						<Unit>60</Unit>

**P375** 					</DevtgSttlmUnit>

**P376** 					<DevtgSttlmUnit>

**P377** 						<Unit>67</Unit>

**P378** 					</DevtgSttlmUnit>

**P379** 				</SttlmInf>

**P380** 			</FinInstrmAttrbts>

**P381** 		</Scty>

**P382** 	</SctyCreReq>

**P383** </Document>

