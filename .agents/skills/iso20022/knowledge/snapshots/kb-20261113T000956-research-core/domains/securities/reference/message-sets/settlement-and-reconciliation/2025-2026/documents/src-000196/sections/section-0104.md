---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "IntraPositionMovementPostingReport semt.016.001.10"]
content_origin: "source-transcription"
---

# IntraPositionMovementPostingReport semt.016.001.10

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path Business Examples / IntraPositionMovementPostingReport semt.016.001.10.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1071** IntraPositionMovementPostingReport semt.016.001.10

**P1072** Description

**P1073** On the 15 January 2019, the account servicer, Dresdner Bank London (DRESGB2L), sends to its customers Dresdner Bank Frankfurt (DRESDEFF) an Intra-Position Movement Posting Report (semt.016.001.06). It is used to confirm the previously requested securities movements (here there is only one) for a specific period of time.

**P1074** Business Data

**P1075** Number of Pages: 1

**P1076** Report Number: 125

**P1077** Statement period from 14/01/2019 to 15/01/2019

**P1078** Frequency of the Report: daily

**P1079** Update Type: Complete

**P1080** Activity Indicator: true

**P1081** Safekeeping Account: 222S

**P1082** Account Owner Transaction Id: FRTJ123REG1

**P1083** Financial Instrument: GB0987654321

**P1084** Position moved: 4,000,000 from the available to the restricted balance 

**P1085** Settlement Date:15/01/2019

**P1086** Message Instance

**P1087** <IntraPosMvmntPstngRpt>

**P1088** 	<Pgntn>

**P1089** 		<PgNb>1</PgNb>

**P1090** 		<LastPgInd>true</LastPgInd>

**P1091** 	</Pgntn>

**P1092** 	<StmtGnlDtls>

**P1093** 		<RptNb>

**P1094** 			<Shrt>125</Shrt>

**P1095** 		</RptNb>

**P1096** 		<StmtPrd>

**P1097** 			<FrDtToDt>

**P1098** 				<FrDt>2019-01-14</FrDt>

**P1099** 				<ToDt>2019-01-15</ToDt>

**P1100** 			</FrDtToDt>

**P1101** 		</StmtPrd>

**P1102** 		<Frqcy>

**P1103** 			<Cd>DAIL</Cd>

**P1104** 		</Frqcy>

**P1105** 		<UpdTp>

**P1106** 			<Cd>COMP</Cd>

**P1107** 		</UpdTp>

**P1108** 		<ActvtyInd>true</ActvtyInd>

**P1109** 	</StmtGnlDtls>

**P1110** 	<SfkpgAcct>

**P1111** 		<Id>222S</Id>

**P1112** 	</SfkpgAcct>

**P1113** 	<FinInstrm>

**P1114** 		<FinInstrmId>

**P1115** 			<ISIN>GB0987654321</ISIN>

**P1116** 		</FinInstrmId>

**P1117** 		<SubBal>

**P1118** 			<BalFr>

**P1119** 				<Cd>AVAI</Cd>

**P1120** 			</BalFr>

**P1121** 			<IntraPosMvmnt>

**P1122** 				<Id>

**P1123** 					<AcctOwnrTxId>FRTJ123REG1</AcctOwnrTxId>

**P1124** 				</Id>

**P1125** 				<SttldQty>

**P1126** 					<FaceAmt>4000000</FaceAmt>

**P1127** 				</SttldQty>

**P1128** 				<BalTo>

**P1129** 					<Cd>RSTR</Cd>

**P1130** 				</BalTo>

**P1131** 				<SttlmDt>

**P1132** 					<Dt>2019-01-15</Dt>

**P1133** 				</SttlmDt>

**P1134** 			</IntraPosMvmnt>

**P1135** 		</SubBal>

**P1136** 	</FinInstrm>

**P1137** </IntraPosMvmntPstngRpt>

