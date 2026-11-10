---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["Business Examples", "Intra Position Movement Query Response (semt.029)"]
content_origin: "source-transcription"
---

# Intra Position Movement Query Response (semt.029)

Source: [src-000380](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Locator: heading path Business Examples / Intra Position Movement Query Response (semt.029).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P345** Intra Position Movement Query Response (semt.029)

**P346** Description

**P347** In this example T2S sends an Intra Position Movement Query Response containing instructions matching the query criteria specified in the query with reference ‘ID0Q0F003452’, which is requesting the full details of movements where securities with an ISIN ‘DE0000000999’ are moved from the deliverable position to a reserved position ‘RSV8’.

**P349** Message Instance

**P350** <IntraPosMvmntQryRspn>

**P351** 		<Pgntn>

**P352** 			<PgNb>1</PgNb>

**P353** 			<LastPgInd>true</LastPgInd>

**P354** 		</Pgntn>

**P355** 		<RptGnlDtls>

**P356** 			<QryRef>ID0Q0F003452</QryRef>

**P357** 			<QryTp>FULL</QryTp>

**P358** 			<ActvtyInd>true</ActvtyInd>

**P359** 		</RptGnlDtls>

**P360** 		<Mvmnts>

**P361** 			<Mvmnt>

**P362** 				<AcctOwnr>

**P363** 					<Id>

**P364** 						<Id>

**P365** 							<AnyBIC>PRYZDEFFXXX</AnyBIC>

**P366** 						</Id>

**P367** 					</Id>

**P368** 					<RspnsblPtyId>

**P369** 						<Id>

**P370** 							<AnyBIC>CSDFDEFFXXX</AnyBIC>

**P371** 						</Id>

**P372** 					</RspnsblPtyId>

**P373** 				</AcctOwnr>

**P374** 				<SfkpgAcct>

**P375** 					<Id>2300000582</Id>

**P376** 				</SfkpgAcct>

**P377** 				<StsAndRsn>

**P378** 					<PrcgSts>

**P379** 						<AckdAccptd>

**P380** 							<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P381** 						</AckdAccptd>

**P382** 					</PrcgSts>

**P383** 					<Sttld/>

**P384** 				</StsAndRsn>

**P385** 				<AcctOwnrTxId>ACCTOWNREF062</AcctOwnrTxId>

**P386** 				<MktInfrstrctrTxId>T2SREF00968320</MktInfrstrctrTxId>

**P387** 				<MvmntDtls>

**P388** 					<BalFr>

**P389** 						<Tp>

**P390** 							<Cd>AWAS</Cd>

**P391** 						</Tp>

**P392** 					</BalFr>

**P393** 					<BalTo>

**P394** 						<Tp>

**P395** 							<Prtry>

**P396** 								<Id>RSV8</Id>

**P397** 								<Issr>T2S</Issr>

**P398** 								<SchmeNm>RT</SchmeNm>

**P399** 							</Prtry>

**P400** 						</Tp>

**P401** 					</BalTo>

**P402** 					<FinInstrmId>

**P403** 						<ISIN>DE0000000999</ISIN>

**P404** 					</FinInstrmId>

**P405** 					<SttlmQty>

**P406** 						<Unit>100000</Unit>

**P407** 					</SttlmQty>

**P408** 					<SttldQty>

**P409** 						<Unit>100000</Unit>

**P410** 					</SttldQty>

**P411** 					<IntnddSttlmDt>

**P412** 						<Dt>2025-02-12</Dt>

**P413** 					</IntnddSttlmDt>

**P414** 					<FctvSttlmDt>

**P415** 						<Dt>2025-02-12</Dt>

**P416** 					</FctvSttlmDt>

**P417** 					<StsDt>2025-02-12T16:20:34</StsDt>

**P418** 					<SctiesSubBalId>

**P419** 						<Id>8243366</Id>

**P420** 					</SctiesSubBalId>

**P421** 					<Prty>

**P422** 						<Nmrc>0004</Nmrc>

**P423** 					</Prty>

**P424** 					<MsgOrgtr>

**P425** 						<Id>

**P426** 							<Id>

**P427** 								<AnyBIC>PRYZDEFFXXX</AnyBIC>

**P428** 							</Id>

**P429** 						</Id>

**P430** 						<RspnsblPtyId>

**P431** 							<Id>

**P432** 								<AnyBIC>CSDFDEFFXXX</AnyBIC>

**P433** 							</Id>

**P434** 						</RspnsblPtyId>

**P435** 					</MsgOrgtr>

**P436** 					<CreDtTm>2025-02-10T08:30:19</CreDtTm>

**P437** 				</MvmntDtls>

**P438** 			</Mvmnt>

**P439** 			<Mvmnt>

**P440** 				<AcctOwnr>

**P441** 					<Id>

**P442** 						<Id>

**P443** 							<AnyBIC>PRYADEFFXXX</AnyBIC>

**P444** 						</Id>

**P445** 					</Id>

**P446** 					<RspnsblPtyId>

**P447** 						<Id>

**P448** 							<AnyBIC>CSDFDEFFXXX</AnyBIC>

**P449** 						</Id>

**P450** 					</RspnsblPtyId>

**P451** 				</AcctOwnr>

**P452** 				<SfkpgAcct>

**P453** 					<Id>2300000582</Id>

**P454** 				</SfkpgAcct>

**P455** 				<StsAndRsn>

**P456** 					<PrcgSts>

**P457** 						<AckdAccptd>

**P458** 							<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P459** 						</AckdAccptd>

**P460** 					</PrcgSts>		

**P461** 				</StsAndRsn>

**P462** 				<AcctOwnrTxId>ACCTOWNREF234</AcctOwnrTxId>

**P463** 				<MktInfrstrctrTxId>T2SREF00723492</MktInfrstrctrTxId>

**P464** 				<MvmntDtls>

**P465** 					<BalFr>

**P466** 						<Tp>

**P467** 							<Cd>AWAS</Cd>

**P468** 						</Tp>

**P469** 					</BalFr>

**P470** 					<BalTo>

**P471** 						<Tp>

**P472** 							<Prtry>

**P473** 								<Id>RSV8</Id>

**P474** 								<Issr>T2S</Issr>

**P475** 								<SchmeNm>RT</SchmeNm>

**P476** 							</Prtry>

**P477** 						</Tp>

**P478** 					</BalTo>

**P479** 					<FinInstrmId>

**P480** 						<ISIN>DE0000000999</ISIN>

**P481** 					</FinInstrmId>

**P482** 					<SttlmQty>

**P483** 						<Unit>23400</Unit>

**P484** 					</SttlmQty>

**P485** 					<IntnddSttlmDt>

**P486** 						<Dt>2025-02-11</Dt>

**P487** 					</IntnddSttlmDt>

**P488** 					<StsDt>2025-02-11T09:15:21</StsDt>

**P489** 					<Prty>

**P490** 						<Nmrc>0004</Nmrc>

**P491** 					</Prty>

**P492** 					<MsgOrgtr>

**P493** 						<Id>

**P494** 							<Id>

**P495** 								<AnyBIC>PRYADEFFXXX</AnyBIC>

**P496** 							</Id>

**P497** 						</Id>

**P498** 						<RspnsblPtyId>

**P499** 							<Id>

**P500** 								<AnyBIC>CSDFDEFFXXX</AnyBIC>

**P501** 							</Id>

**P502** 						</RspnsblPtyId>

**P503** 					</MsgOrgtr>

**P504** 					<CreDtTm>2025-02-11T08:45:43</CreDtTm>

**P505** 				</MvmntDtls>

**P506** 			</Mvmnt>

**P507** 			<Mvmnt>

**P508** 				<AcctOwnr>

**P509** 					<Id>

**P510** 						<Id>

**P511** 							<AnyBIC>PRYZDEFFXXX</AnyBIC>

**P512** 						</Id>

**P513** 					</Id>

**P514** 					<RspnsblPtyId>

**P515** 						<Id>

**P516** 							<AnyBIC>CSDFDEFFXXX</AnyBIC>

**P517** 						</Id>

**P518** 					</RspnsblPtyId>

**P519** 				</AcctOwnr>

**P520** 				<SfkpgAcct>

**P521** 					<Id>2300000582</Id>

**P522** 				</SfkpgAcct>

**P523** 				<StsAndRsn>

**P524** 					<PrcgSts>

**P525** 						<AckdAccptd>

**P526** 							<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P527** 						</AckdAccptd>

**P528** 					</PrcgSts>

**P529** 					<Sttld/>

**P530** 				</StsAndRsn>

**P531** 				<AcctOwnrTxId>ACCTOWNREF072</AcctOwnrTxId>

**P532** 				<MktInfrstrctrTxId>T2SREF00967346</MktInfrstrctrTxId>

**P533** 				<MvmntDtls>

**P534** 					<BalFr>

**P535** 						<Tp>

**P536** 							<Cd>AWAS</Cd>

**P537** 						</Tp>

**P538** 					</BalFr>

**P539** 					<BalTo>

**P540** 						<Tp>

**P541** 							<Prtry>

**P542** 								<Id>RSV8</Id>

**P543** 								<Issr>T2S</Issr>

**P544** 								<SchmeNm>RT</SchmeNm>

**P545** 							</Prtry>

**P546** 						</Tp>

**P547** 					</BalTo>

**P548** 					<FinInstrmId>

**P549** 						<ISIN>DE0000000999</ISIN>

**P550** 					</FinInstrmId>

**P551** 					<SttlmQty>

**P552** 						<Unit>54000</Unit>

**P553** 					</SttlmQty>

**P554** 					<SttldQty>

**P555** 						<Unit>54000</Unit>

**P556** 					</SttldQty>

**P557** 					<IntnddSttlmDt>

**P558** 						<Dt>2025-02-13</Dt>

**P559** 					</IntnddSttlmDt>

**P560** 					<FctvSttlmDt>

**P561** 						<Dt>2025-02-13</Dt>

**P562** 					</FctvSttlmDt>

**P563** 					<StsDt>2025-02-13T12:41:59</StsDt>

**P564** 					<SctiesSubBalId>

**P565** 						<Id>8243366</Id>

**P566** 					</SctiesSubBalId>

**P567** 					<Prty>

**P568** 						<Nmrc>0003</Nmrc>

**P569** 					</Prty>

**P570** 					<MsgOrgtr>

**P571** 						<Id>

**P572** 							<Id>

**P573** 								<AnyBIC>PRYZDEFFXXX</AnyBIC>

**P574** 							</Id>

**P575** 						</Id>

**P576** 						<RspnsblPtyId>

**P577** 							<Id>

**P578** 								<AnyBIC>CSDFDEFFXXX</AnyBIC>

**P579** 							</Id>

**P580** 						</RspnsblPtyId>

**P581** 					</MsgOrgtr>

**P582** 					<CreDtTm>2025-02-13T10:05:51</CreDtTm>

**P583** 				</MvmntDtls>

**P584** 			</Mvmnt>

**P585** 			<Mvmnt>

**P586** 				<AcctOwnr>

**P587** 					<Id>

**P588** 						<Id>

**P589** 							<AnyBIC>PRYZDEFFXXX</AnyBIC>

**P590** 						</Id>

**P591** 					</Id>

**P592** 					<RspnsblPtyId>

**P593** 						<Id>

**P594** 							<AnyBIC>CSDFDEFFXXX</AnyBIC>

**P595** 						</Id>

**P596** 					</RspnsblPtyId>

**P597** 				</AcctOwnr>

**P598** 				<SfkpgAcct>

**P599** 					<Id>2300000714</Id>

**P600** 				</SfkpgAcct>

**P601** 				<StsAndRsn>

**P602** 					<PrcgSts>

**P603** 						<AckdAccptd>

**P604** 							<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P605** 						</AckdAccptd>

**P606** 					</PrcgSts>

**P607** 					<Sttld/>

**P608** 				</StsAndRsn>

**P609** 				<AcctOwnrTxId>ACCTOWNREF980</AcctOwnrTxId>

**P610** 				<MktInfrstrctrTxId>T2SREF00976231</MktInfrstrctrTxId>

**P611** 				<MvmntDtls>

**P612** 					<BalFr>

**P613** 						<Tp>

**P614** 							<Cd>AWAS</Cd>

**P615** 						</Tp>

**P616** 					</BalFr>

**P617** 					<BalTo>

**P618** 						<Tp>

**P619** 							<Prtry>

**P620** 								<Id>RSV8</Id>

**P621** 								<Issr>T2S</Issr>

**P622** 								<SchmeNm>RT</SchmeNm>

**P623** 							</Prtry>

**P624** 						</Tp>

**P625** 					</BalTo>

**P626** 					<FinInstrmId>

**P627** 						<ISIN>DE0000000999</ISIN>

**P628** 					</FinInstrmId>

**P629** 					<SttlmQty>

**P630** 						<Unit>10500</Unit>

**P631** 					</SttlmQty>

**P632** 					<SttldQty>

**P633** 						<Unit>10500</Unit>

**P634** 					</SttldQty>

**P635** 					<IntnddSttlmDt>

**P636** 						<Dt>2025-02-17</Dt>

**P637** 					</IntnddSttlmDt>

**P638** 					<FctvSttlmDt>

**P639** 						<Dt>2025-02-17</Dt>

**P640** 					</FctvSttlmDt>

**P641** 					<StsDt>2025-02-17T13:32:14</StsDt>

**P642** 					<SctiesSubBalId>

**P643** 						<Id>8255362</Id>

**P644** 					</SctiesSubBalId>

**P645** 					<Prty>

**P646** 						<Nmrc>0004</Nmrc>

**P647** 					</Prty>

**P648** 					<MsgOrgtr>

**P649** 						<Id>

**P650** 							<Id>

**P651** 								<AnyBIC>PRYZDEFFXXX</AnyBIC>

**P652** 							</Id>

**P653** 						</Id>

**P654** 						<RspnsblPtyId>

**P655** 							<Id>

**P656** 								<AnyBIC>CSDFDEFFXXX</AnyBIC>

**P657** 							</Id>

**P658** 						</RspnsblPtyId>

**P659** 					</MsgOrgtr>

**P660** 					<CreDtTm>2025-02-14T15:27:32</CreDtTm>

**P661** 				</MvmntDtls>

**P662** 			</Mvmnt>

**P663** 			<Mvmnt>

**P664** 				<AcctOwnr>

**P665** 					<Id>

**P666** 						<Id>

**P667** 							<AnyBIC>PRYZDEFFXXX</AnyBIC>

**P668** 						</Id>

**P669** 					</Id>

**P670** 					<RspnsblPtyId>

**P671** 						<Id>

**P672** 							<AnyBIC>CSDFDEFFXXX</AnyBIC>

**P673** 						</Id>

**P674** 					</RspnsblPtyId>

**P675** 				</AcctOwnr>

**P676** 				<SfkpgAcct>

**P677** 					<Id>2300000714</Id>

**P678** 				</SfkpgAcct>

**P679** 				<StsAndRsn>

**P680** 					<PrcgSts>

**P681** 						<AckdAccptd>

**P682** 							<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P683** 						</AckdAccptd>

**P684** 					</PrcgSts>

**P685** 				</StsAndRsn>

**P686** 				<AcctOwnrTxId>ACCTOWNREF997</AcctOwnrTxId>

**P687** 				<MktInfrstrctrTxId>T2SREF00977451</MktInfrstrctrTxId>

**P688** 				<MvmntDtls>

**P689** 					<BalFr>

**P690** 						<Tp>

**P691** 							<Cd>AWAS</Cd>

**P692** 						</Tp>

**P693** 					</BalFr>

**P694** 					<BalTo>

**P695** 						<Tp>

**P696** 							<Prtry>

**P697** 								<Id>RSV8</Id>

**P698** 								<Issr>T2S</Issr>

**P699** 								<SchmeNm>RT</SchmeNm>

**P700** 							</Prtry>

**P701** 						</Tp>

**P702** 					</BalTo>

**P703** 					<FinInstrmId>

**P704** 						<ISIN>DE0000000999</ISIN>

**P705** 					</FinInstrmId>

**P706** 					<SttlmQty>

**P707** 						<Unit>10500</Unit>

**P708** 					</SttlmQty>

**P709** 					<IntnddSttlmDt>

**P710** 						<Dt>2025-02-18</Dt>

**P711** 					</IntnddSttlmDt>

**P712** 					<StsDt>2025-02-17T18:25:01</StsDt>

**P713** 					<SctiesSubBalId>

**P714** 						<Id>8255362</Id>

**P715** 					</SctiesSubBalId>

**P716** 					<Prty>

**P717** 						<Nmrc>0002</Nmrc>

**P718** 					</Prty>

**P719** 					<MsgOrgtr>

**P720** 						<Id>

**P721** 							<Id>

**P722** 								<AnyBIC>PRYZDEFFXXX</AnyBIC>

**P723** 							</Id>

**P724** 						</Id>

**P725** 						<RspnsblPtyId>

**P726** 							<Id>

**P727** 								<AnyBIC>CSDFDEFFXXX</AnyBIC>

**P728** 							</Id>

**P729** 						</RspnsblPtyId>

**P730** 					</MsgOrgtr>

**P731** 					<CreDtTm>2025-02-17T17:59:40</CreDtTm>

**P732** 				</MvmntDtls>

**P733** 			</Mvmnt>

**P734** 		</Mvmnts>

**P735** </IntraPosMvmntQryRspn>

