---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Intra-balance Movement Instruction - camt.066.001"]
content_origin: "source-transcription"
---

# Intra-balance Movement Instruction - camt.066.001

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Examples / Intra-balance Movement Instruction - camt.066.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P320** Intra-balance Movement Instruction - camt.066.001

**P321** Description

**P322** In this example, Party A “PRTYABICXXX” has requested, using a transaction id ‘REF0123’, the blocking of 50000 EUR, within a pool with reference ‘POOL1234’, with a normal priority for the restriction type ‘BLKA’, on the 9th of January 2015 within its account ‘9000000123’.

**P323** Message instance

**P324** <Document>

**P325**        <IntraBalMvmntInstr>

**P326** 		<Id>

**P327** 			<TxId>REF0123</TxId>

**P328** 			<DocId>ID0ABCD</DocId>

**P329** 		</Id>

**P330** 		<NbCounts>

**P331** 			<TtlNb>

**P332** 				<CurInstrNb>002</CurInstrNb>

**P333** 				<TtlOfLkdInstrs>005</TtlOfLkdInstrs>

**P334** 			</TtlNb>

**P335** 		</NbCounts>

**P336** 		<Lnkgs>

**P337** 			<PrcgPos>

**P338** 				<Cd>WITH</Cd>

**P339** 			</PrcgPos>

**P340** 			<Ref>

**P341** 				<PoolId>POOL1234</PoolId>

**P342** 			</Ref>

**P343** 			<RefOwnr>

**P344** 				<AnyBIC>PRTYXBICXXX</AnyBIC>

**P345** 			</RefOwnr>

**P346** 		</Lnkgs>

**P347** 		<CshAcct>

**P348** 			<Id>

**P349** 				<Othr>

**P350** 					<Id>9000000123</Id>

**P351** 				</Othr>

**P352** 			</Id>

**P353** 		</CshAcct>

**P354** 		<CshAcctOwnr>

**P355** 			<Id>

**P356** 				<Id>

**P357** 					<AnyBIC>PRTYABICXXX</AnyBIC>

**P358** 				</Id>

**P359** 			</Id>

**P360** 		</CshAcctOwnr>

**P361** 		<IntraBal>

**P362** 			<SttlmAmt>

**P363** 				<AmtWthCcy Ccy="EUR">50000</AmtWthCcy>

**P364** 			</SttlmAmt>

**P365** 			<SttlmDt>

**P366** 				<Dt>2015-01-09</Dt>

**P367** 			</SttlmDt>

**P368** 			<BalFr>

**P369** 				<Tp>

**P370** 					<Prtry>

**P371** 						<Id>DLVR</Id>

**P372** 						<Issr>T2S</Issr>

**P373** 						<SchmeNm>RT</SchmeNm>

**P374** 					</Prtry>

**P375** 				</Tp>

**P376** 			</BalFr>

**P377** 			<BalTo>

**P378** 				<Tp>

**P379** 					<Prtry>

**P380** 						<Id>BLKA</Id>

**P381** 						<Issr>T2S</Issr>

**P382** 						<SchmeNm>RT</SchmeNm>

**P383** 					</Prtry>

**P384** 				</Tp>

**P385** 			</BalTo>

**P386** 			<Prty>

**P387** 				<Nmrc>0004</Nmrc>

**P388** 			</Prty>

**P389** 		</IntraBal>

**P390** 	</IntraBalMvmntInstr>

**P391** </Document>

