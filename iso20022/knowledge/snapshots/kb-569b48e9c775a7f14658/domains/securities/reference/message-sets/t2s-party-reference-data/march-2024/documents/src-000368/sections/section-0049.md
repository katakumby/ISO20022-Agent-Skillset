---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Business Examples", "Party Activity Advice - reda.041.001"]
content_origin: "source-transcription"
---

# Party Activity Advice - reda.041.001

Source: [src-000368](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Locator: heading path Business Examples / Party Activity Advice - reda.041.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P586** Party Activity Advice - reda.041.001

**P587** Description

**P588** The PartyActivityAdvice (reda.041) message provides information on changes occurred for party reference data during the business day. In this example, it shows two changes occurred on 2017-08-23 to the party PAYBXXYYAAA regarding the Party Long Name and its validity:

**P589** System date: 2017-08-23

**P590** First change:

**P591** Field changed: PartyName.ValidFrom

**P592** Party ID: BANKXXYYAAA

**P593** Responsible Party ID: NCBAXXYYAAA

**P594** Old Filed Value: 2008-07-01

**P595** New Field Value: 2017-08-23

**P596** Timestamp of the Update performed: 2017-08-23T15:10:10

**P597** Second change:

**P598** Field changed: PartyName.LongName

**P599** Party ID: BANKXXYYAAA

**P600** Responsible Party ID: NCBAXXYYAAA

**P601** Old Filed Value: SAMPLE NAME

**P602** New Field Value: NEW SAMPLE NAME

**P603** Timestamp of the Update performed: 2017-08-23T16:30:10

**P604** Message Instance

**P605** <Document>

**P606** 	<PtyActvtyAdvc>

**P607** 		<MsgHdr>

**P608** 			<MsgId>SAMPLEPTYSTA</MsgId>

**P609** 		</MsgHdr>

**P610** 		<PtyActvty>

**P611** 			<SysDt>2017-08-23</SysDt>

**P612** 			<Chng>

**P613** 				<PtyId>

**P614** 					<Id>

**P615** 						<Id>

**P616** 							<AnyBIC>PAYBXXYYAAA</AnyBIC>

**P617** 						</Id>

**P618** 					</Id>

**P619** 					<RspnsblPtyId>

**P620** 						<Id>

**P621** 							<AnyBIC>NCBAXXYYAAA</AnyBIC>

**P622** 						</Id>

**P623** 					</RspnsblPtyId>

**P624** 				</PtyId>

**P625** 				<Rcrd>

**P626** 					<Othr>

**P627** 						<FldNm>PartyName.ValidFrom</FldNm>

**P628** 						<OdFldVal>2008-07-01</OdFldVal>

**P629** 						<NewFldVal>2017-08-23</NewFldVal>						

**P630** 					</Othr>					

**P631** 				</Rcrd>				

**P632** 				<OprTmStmp>2017-08-23T15:10:10</OprTmStmp>

**P633** 			</Chng>

**P634** 			<Chng>

**P635** 				<PtyId>

**P636** 					<Id>

**P637** 						<Id>

**P638** 							<AnyBIC>PAYBXXYYAAA</AnyBIC>

**P639** 						</Id>

**P640** 					</Id>

**P641** 					<RspnsblPtyId>

**P642** 						<Id>

**P643** 							<AnyBIC>NCBAXXYYAAA</AnyBIC>

**P644** 						</Id>

**P645** 					</RspnsblPtyId>

**P646** 				</PtyId>

**P647** 				<Rcrd>

**P648** 					<Othr>

**P649** 						<FldNm>PartyName.LongName</FldNm>

**P650** 						<OdFldVal>SAMPLE NAME</OdFldVal>

**P651** 						<NewFldVal>NEW SAMPLE NAME</NewFldVal>

**P652** 					</Othr>

**P653** 				</Rcrd>

**P654** 				<OprTmStmp>2017-08-23T16:30:10</OprTmStmp>

**P655** 			</Chng>

**P656** 		</PtyActvty>

**P657** 	</PtyActvtyAdvc>

**P658** </Document>

**P659**   


