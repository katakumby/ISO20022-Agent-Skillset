---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["Business Examples", "Securities Settlement Transaction Query Response (semt.027)"]
content_origin: "source-transcription"
---

# Securities Settlement Transaction Query Response (semt.027)

Source: [src-000374](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Locator: heading path Business Examples / Securities Settlement Transaction Query Response (semt.027).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P414** Securities Settlement Transaction Query Response (semt.027)

**P415** The Securities Settlement Transaction Query Response message covers the following T2S message usages depending on the [Query Type] defined in the query:

**P418** Query Response Example: Settlement Instruction Query Response

**P419** Description

**P420** In this example T2S sends a Settlement Instruction Query Response containing one instruction matching the query criteria corresponding to query reference ‘QRYREF0001’. This message is sent as a response to a Settlement Instruction Query requesting all settlement instructions where the securities account is ‘1000000123’ and the settlement quantity is greater than or equal to 50000 units and less than or equal to 60000 units.

**P422** Message Instance

**P424** <SctiesSttlmTxQryRspn>

**P425** 	<Pgntn>

**P426** 		<PgNb>1</PgNb>

**P427** 		<LastPgInd>true</LastPgInd>

**P428** 	</Pgntn>

**P429** 	<RptGnlDtls>

**P430** 		<QryRef>QRYREF0001</QryRef>

**P431** 		<QryTp>INST</QryTp>

**P432** 		<ActvtyInd>true</ActvtyInd>

**P433** 	</RptGnlDtls>

**P434** 	<Txs>

**P435** 		<Tx>

**P436** 			<SfkpgAcct>

**P437** 				<Id>1000000123</Id>

**P438** 			</SfkpgAcct>

**P439** 			<StsAndRsn>

**P440** 				<MtchgSts>

**P441** 					<Mtchd/>

**P442** 				</MtchgSts>

**P443** 				<Sttld/>

**P444** 			</StsAndRsn>

**P445** 			<AcctOwnrTxId>NONREF</AcctOwnrTxId>

**P446** 			<AcctSvcrTxId>INITSEMT026-002</AcctSvcrTxId>

**P447** 			<MktInfrstrctrTxId>2306130527746616</MktInfrstrctrTxId>

**P448** 			<TxDtls>

**P449** 				<TxActvty>

**P450** 					<Cd>SETT</Cd>

**P451** 				</TxActvty>

**P452** 				<SttlmTxOrCorpActnEvtTp>

**P453** 					<SctiesTxTp>

**P454** 						<Cd>TRAD</Cd>

**P455** 					</SctiesTxTp>

**P456** 				</SttlmTxOrCorpActnEvtTp>

**P457** 				<SctiesMvmntTp>RECE</SctiesMvmntTp>

**P458** 				<Pmt>FREE</Pmt>

**P459** 				<FinInstrmId>

**P460** 					<ISIN>ISIN00000456</ISIN>

**P461** 				</FinInstrmId>

**P462** 				<SttlmQty>

**P463** 					<Unit>52650</Unit>

**P464** 				</SttlmQty>

**P465** 				<SttldQty>

**P466** 					<Unit>52650</Unit>

**P467** 				</SttldQty>

**P468** 				<PrevslySttldQty>

**P469** 					<Unit>0</Unit>

**P470** 				</PrevslySttldQty>

**P471** 				<RmngToBeSttldQty>

**P472** 					<Unit>0</Unit>

**P473** 				</RmngToBeSttldQty>

**P474** 				<SttlmAmt>

**P475** 					<Amt Ccy="EUR">0</Amt>

**P476** 				</SttlmAmt>

**P477** 				<TradDt>

**P478** 					<Dt>

**P479** 						<Dt>2025-09-25</Dt>

**P480** 					</Dt>

**P481** 				</TradDt>

**P482** 				<IntnddSttlmDt>

**P483** 					<Dt>

**P484** 						<Dt>2025-09-25</Dt>

**P485** 					</Dt>

**P486** 				</IntnddSttlmDt>

**P487** 				<FctvSttlmDt>

**P488** 					<Dt>2025-09-25</Dt>

**P489** 				</FctvSttlmDt>

**P490** 				<AckdStsTmStmp>2025-09-25T18:04:41.492392</AckdStsTmStmp>

**P491** 				<MtchdStsTmStmp>2025-09-25T18:04:41.511189</MtchdStsTmStmp>

**P492** 				<Prty>

**P493** 					<Nmrc>0004</Nmrc>

**P494** 				</Prty>

**P495** 				<DlvrgSttlmPties>

**P496** 					<Dpstry>

**P497** 						<Id>

**P498** 							<AnyBIC>PAAHPFP1000</AnyBIC>

**P499** 						</Id>

**P500** 					</Dpstry>

**P501** 					<Pty1>

**P502** 						<Id>

**P503** 							<AnyBIC>PAAHPFP1000</AnyBIC>

**P504** 						</Id>

**P505** 						<SfkpgAcct>

**P506** 							<Id>C5PFISSA362070</Id>

**P507** 						</SfkpgAcct>

**P508** 					</Pty1>

**P509** 				</DlvrgSttlmPties>

**P510** 				<RcvgSttlmPties>

**P511** 					<Dpstry>

**P512** 						<Id>

**P513** 							<AnyBIC>PAAHPFP1000</AnyBIC>

**P514** 						</Id>

**P515** 					</Dpstry>

**P516** 					<Pty1>

**P517** 						<Id>

**P518** 							<AnyBIC>PALLPFP1000</AnyBIC>

**P519** 						</Id>

**P520** 						<SfkpgAcct>

**P521** 							<Id>1000000123</Id>

**P522** 						</SfkpgAcct>

**P523** 					</Pty1>

**P524** 				</RcvgSttlmPties>

**P525** 				<MsgOrgtr>

**P526** 					<Id>

**P527** 						<Id>

**P528** 							<AnyBIC>PAAHPFP1000</AnyBIC>

**P529** 						</Id>

**P530** 					</Id>

**P531** 					<RspnsblPtyId>

**P532** 						<Id>

**P533** 							<AnyBIC>TCSOTCS0XXX</AnyBIC>

**P534** 						</Id>

**P535** 					</RspnsblPtyId>

**P536** 				</MsgOrgtr>

**P537** 				<CreDtTm>2025-09-25T18:04:39.676727</CreDtTm>

**P538** 			</TxDtls>

**P539** 		</Tx>

**P540** 	</Txs>

**P541** </SctiesSttlmTxQryRspn>

**P543** Query Response Example: Settlement Instruction Current Status Query Response

**P544** Description

**P545** In this example T2S sends a Settlement Instruction Current Status Query Response containing one instruction matching the query criteria corresponding to query reference ‘QRYREF0002’. This message is sent as a response to a Settlement Instruction Current Status Query requesting all pending settlement instructions with a high priority where the securities account is ‘1000000123’.

**P547** Message Instance

**P549** <SctiesSttlmTxQryRspn>

**P550** 	<Pgntn>

**P551** 		<PgNb>1</PgNb>

**P552** 		<LastPgInd>true</LastPgInd>

**P553** 	</Pgntn>

**P554** 	<RptGnlDtls>

**P555** 		<QryRef>QRYREF0002</QryRef>

**P556** 		<QryTp>STTS</QryTp>

**P557** 		<ActvtyInd>true</ActvtyInd>

**P558** 	</RptGnlDtls>

**P559** 	<Txs>

**P560** 		<StsAndRsn>

**P561** 			<SttlmSts>

**P562** 				<Pdg>

**P563** 					<Rsn>

**P564** 						<Cd>

**P565** 							<Cd>LACK</Cd>

**P566** 						</Cd>

**P567** 						<AddtlRsnInf>SXAA014 - Failure of the settlement attempt of the settlement instruction due to a lack of securities in your securities position</AddtlRsnInf>

**P568** 					</Rsn>

**P569** 				</Pdg>

**P570** 			</SttlmSts>

**P571** 		</StsAndRsn>

**P572** 		<Tx>

**P573** 			<SfkpgAcct>

**P574** 				<Id>1000000123</Id>

**P575** 			</SfkpgAcct>

**P576** 			<StsAndRsn>

**P577** 				<MtchgSts>

**P578** 					<Mtchd/>

**P579** 				</MtchgSts>

**P580** 				<SttlmSts>

**P581** 					<Pdg>

**P582** 						<Rsn>

**P583** 							<Cd>

**P584** 								<Cd>LACK</Cd>

**P585** 							</Cd>

**P586** 							<AddtlRsnInf>SXAA014 - Failure of the settlement attempt of the settlement instruction due to a lack of securities in your securities position</AddtlRsnInf>

**P587** 						</Rsn>

**P588** 					</Pdg>

**P589** 				</SttlmSts>

**P590** 			</StsAndRsn>

**P591** 			<AcctOwnrTxId>TESTSEMT026-001</AcctOwnrTxId>

**P592** 			<MktInfrstrctrTxId>2306130527744846</MktInfrstrctrTxId>

**P593** 			<TxDtls>

**P594** 				<TxActvty>

**P595** 					<Cd>SETT</Cd>

**P596** 				</TxActvty>

**P597** 				<SttlmTxOrCorpActnEvtTp>

**P598** 					<SctiesTxTp>

**P599** 						<Cd>TRAD</Cd>

**P600** 					</SctiesTxTp>

**P601** 				</SttlmTxOrCorpActnEvtTp>

**P602** 				<SctiesMvmntTp>DELI</SctiesMvmntTp>

**P603** 				<Pmt>FREE</Pmt>

**P604** 				<FinInstrmId>

**P605** 					<ISIN>PF0003625005</ISIN>

**P606** 				</FinInstrmId>

**P607** 				<SttlmQty>

**P608** 					<FaceAmt>54000.00</FaceAmt>

**P609** 				</SttlmQty>

**P610** 				<SttldQty>

**P611** 					<FaceAmt>0</FaceAmt>

**P612** 				</SttldQty>

**P613** 				<PrevslySttldQty>

**P614** 					<FaceAmt>0</FaceAmt>

**P615** 				</PrevslySttldQty>

**P616** 				<RmngToBeSttldQty>

**P617** 					<FaceAmt>54000</FaceAmt>

**P618** 				</RmngToBeSttldQty>

**P619** 				<SttlmAmt>

**P620** 					<Amt Ccy="EUR">0</Amt>

**P621** 				</SttlmAmt>

**P622** 				<TradDt>

**P623** 					<Dt>

**P624** 						<Dt>2025-09-25</Dt>

**P625** 					</Dt>

**P626** 				</TradDt>

**P627** 				<IntnddSttlmDt>

**P628** 					<Dt>

**P629** 						<Dt>2025-09-25</Dt>

**P630** 					</Dt>

**P631** 				</IntnddSttlmDt>

**P632** 				<StsDt>2025-09-24T15:06:52.976484</StsDt>

**P633** 				<AckdStsTmStmp>2025-09-23T17:22:28.964428</AckdStsTmStmp>

**P634** 				<MtchdStsTmStmp>2025-09-23T17:22:28.971750</MtchdStsTmStmp>

**P635** 				<Prty>

**P636** 					<Nmrc>0003</Nmrc>

**P637** 				</Prty>

**P638** 				<DlvrgSttlmPties>

**P639** 					<Dpstry>

**P640** 						<Id>

**P641** 							<AnyBIC>PAAHPFP1000</AnyBIC>

**P642** 						</Id>

**P643** 					</Dpstry>

**P644** 					<Pty1>

**P645** 						<Id>

**P646** 							<AnyBIC>PALLPFP1000</AnyBIC>

**P647** 						</Id>

**P648** 						<SfkpgAcct>

**P649** 							<Id>1000000123</Id>

**P650** 						</SfkpgAcct>

**P651** 					</Pty1>

**P652** 				</DlvrgSttlmPties>

**P653** 				<RcvgSttlmPties>

**P654** 					<Dpstry>

**P655** 						<Id>

**P656** 							<AnyBIC>PAAHPFP1000</AnyBIC>

**P657** 						</Id>

**P658** 					</Dpstry>

**P659** 					<Pty1>

**P660** 						<Id>

**P661** 							<AnyBIC>PALLPFP1000</AnyBIC>

**P662** 						</Id>

**P663** 						<SfkpgAcct>

**P664** 							<Id>C5PFCSDP370670</Id>

**P665** 						</SfkpgAcct>

**P666** 					</Pty1>

**P667** 				</RcvgSttlmPties>

**P668** 				<MsgOrgtr>

**P669** 					<Id>

**P670** 						<Id>

**P671** 							<AnyBIC>PALLPFP1000</AnyBIC>

**P672** 						</Id>

**P673** 					</Id>

**P674** 					<RspnsblPtyId>

**P675** 						<Id>

**P676** 							<AnyBIC>PAAHPFP1000</AnyBIC>

**P677** 						</Id>

**P678** 					</RspnsblPtyId>

**P679** 				</MsgOrgtr>

**P680** 				<CreDtTm>2025-09-23T17:22:26.722108</CreDtTm>

**P681** 			</TxDtls>

**P682** 		</Tx>

**P683** 	</Txs>

**P684** </SctiesSttlmTxQryRspn>

**P686** Query Response Example: Settlement Instruction Status Audit Trail Query

**P687** Description

**P688** In this example T2S sends a Settlement Instruction Status Audit Trail Query Response containing two instructions matching the query criteria corresponding to query reference ‘QRYREF0003’. This message is sent as a response to a Settlement Instruction Status Audit Trail Query requesting all settlement instructions that were matched on or before the 25th of September 2025.

**P690** Message Instance

**P692** <SctiesSttlmTxQryRspn>

**P693** 	<Pgntn>

**P694** 		<PgNb>1</PgNb>

**P695** 		<LastPgInd>true</LastPgInd>

**P696** 	</Pgntn>

**P697** 	<RptGnlDtls>

**P698** 		<QryRef>QRYREF0003</QryRef>

**P699** 		<QryTp>STPD</QryTp>

**P700** 		<ActvtyInd>true</ActvtyInd>

**P701** 	</RptGnlDtls>

**P702** 	<Txs>

**P703** 		<StsAndRsn>

**P704** 			<MtchgSts>

**P705** 				<Mtchd/>

**P706** 			</MtchgSts>

**P707** 			<Sttld/>

**P708** 		</StsAndRsn>

**P709** 		<Tx>

**P710** 			<SfkpgAcct>

**P711** 				<Id>1000000123</Id>

**P712** 			</SfkpgAcct>

**P713** 			<StsAndRsn>

**P714** 				<MtchgSts>

**P715** 					<Mtchd/>

**P716** 				</MtchgSts>

**P717** 				<Sttld/>

**P718** 			</StsAndRsn>

**P719** 			<AcctOwnrTxId>NONREF</AcctOwnrTxId>

**P720** 			<AcctSvcrTxId>INITSEMT026-002</AcctSvcrTxId>

**P721** 			<MktInfrstrctrTxId>2306130527746616</MktInfrstrctrTxId>

**P722** 			<TxDtls>

**P723** 				<TxActvty>

**P724** 					<Cd>SETT</Cd>

**P725** 				</TxActvty>

**P726** 				<SttlmTxOrCorpActnEvtTp>

**P727** 					<SctiesTxTp>

**P728** 						<Cd>TRAD</Cd>

**P729** 					</SctiesTxTp>

**P730** 				</SttlmTxOrCorpActnEvtTp>

**P731** 				<SctiesMvmntTp>RECE</SctiesMvmntTp>

**P732** 				<Pmt>FREE</Pmt>

**P733** 				<FinInstrmId>

**P734** 					<ISIN>ISIN00000456</ISIN>

**P735** 				</FinInstrmId>

**P736** 				<SttlmQty>

**P737** 					<Unit>52650</Unit>

**P738** 				</SttlmQty>

**P739** 				<SttldQty>

**P740** 					<Unit>52650</Unit>

**P741** 				</SttldQty>

**P742** 				<PrevslySttldQty>

**P743** 					<Unit>0</Unit>

**P744** 				</PrevslySttldQty>

**P745** 				<RmngToBeSttldQty>

**P746** 					<Unit>0</Unit>

**P747** 				</RmngToBeSttldQty>

**P748** 				<SttlmAmt>

**P749** 					<Amt Ccy="EUR">0</Amt>

**P750** 				</SttlmAmt>

**P751** 				<TradDt>

**P752** 					<Dt>

**P753** 						<Dt>2025-09-23</Dt>

**P754** 					</Dt>

**P755** 				</TradDt>

**P756** 				<IntnddSttlmDt>

**P757** 					<Dt>

**P758** 						<Dt>2025-09-23</Dt>

**P759** 					</Dt>

**P760** 				</IntnddSttlmDt>

**P761** 				<FctvSttlmDt>

**P762** 					<Dt>2025-09-23</Dt>

**P763** 				</FctvSttlmDt>

**P764** 				<AckdStsTmStmp>2025-09-23T18:04:41.492392</AckdStsTmStmp>

**P765** 				<MtchdStsTmStmp>2025-09-23T18:04:41.511189</MtchdStsTmStmp>

**P766** 				<Prty>

**P767** 					<Nmrc>0004</Nmrc>

**P768** 				</Prty>

**P769** 				<DlvrgSttlmPties>

**P770** 					<Dpstry>

**P771** 						<Id>

**P772** 							<AnyBIC>PAAHPFP1000</AnyBIC>

**P773** 						</Id>

**P774** 					</Dpstry>

**P775** 					<Pty1>

**P776** 						<Id>

**P777** 							<AnyBIC>PAAHPFP1000</AnyBIC>

**P778** 						</Id>

**P779** 						<SfkpgAcct>

**P780** 							<Id>C5PFISSA362070</Id>

**P781** 						</SfkpgAcct>

**P782** 					</Pty1>

**P783** 				</DlvrgSttlmPties>

**P784** 				<RcvgSttlmPties>

**P785** 					<Dpstry>

**P786** 						<Id>

**P787** 							<AnyBIC>PAAHPFP1000</AnyBIC>

**P788** 						</Id>

**P789** 					</Dpstry>

**P790** 					<Pty1>

**P791** 						<Id>

**P792** 							<AnyBIC>PALLPFP1000</AnyBIC>

**P793** 						</Id>

**P794** 						<SfkpgAcct>

**P795** 							<Id>1000000123</Id>

**P796** 						</SfkpgAcct>

**P797** 					</Pty1>

**P798** 				</RcvgSttlmPties>

**P799** 				<MsgOrgtr>

**P800** 					<Id>

**P801** 						<Id>

**P802** 							<AnyBIC>PAAHPFP1000</AnyBIC>

**P803** 						</Id>

**P804** 					</Id>

**P805** 					<RspnsblPtyId>

**P806** 						<Id>

**P807** 							<AnyBIC>TCSOTCS0XXX</AnyBIC>

**P808** 						</Id>

**P809** 					</RspnsblPtyId>

**P810** 				</MsgOrgtr>

**P811** 				<CreDtTm>2025-09-23T18:04:39.676727</CreDtTm>

**P812** 			</TxDtls>

**P813** 		</Tx>

**P814** 		<Tx>

**P815** 			<SfkpgAcct>

**P816** 				<Id>1000000123</Id>

**P817** 			</SfkpgAcct>

**P818** 			<StsAndRsn>

**P819** 				<MtchgSts>

**P820** 					<Mtchd/>

**P821** 				</MtchgSts>

**P822** 				<Sttld/>

**P823** 			</StsAndRsn>

**P824** 			<AcctOwnrTxId>NONREF</AcctOwnrTxId>

**P825** 			<AcctSvcrTxId>INITSEMT026-001</AcctSvcrTxId>

**P826** 			<MktInfrstrctrTxId>2306130527746201</MktInfrstrctrTxId>

**P827** 			<TxDtls>

**P828** 				<TxActvty>

**P829** 					<Cd>SETT</Cd>

**P830** 				</TxActvty>

**P831** 				<SttlmTxOrCorpActnEvtTp>

**P832** 					<SctiesTxTp>

**P833** 						<Cd>TRAD</Cd>

**P834** 					</SctiesTxTp>

**P835** 				</SttlmTxOrCorpActnEvtTp>

**P836** 				<SctiesMvmntTp>RECE</SctiesMvmntTp>

**P837** 				<Pmt>FREE</Pmt>

**P838** 				<FinInstrmId>

**P839** 					<ISIN>PF0003625005</ISIN>

**P840** 				</FinInstrmId>

**P841** 				<SttlmQty>

**P842** 					<FaceAmt>52650.00</FaceAmt>

**P843** 				</SttlmQty>

**P844** 				<SttldQty>

**P845** 					<FaceAmt>52650.00</FaceAmt>

**P846** 				</SttldQty>

**P847** 				<PrevslySttldQty>

**P848** 					<FaceAmt>0</FaceAmt>

**P849** 				</PrevslySttldQty>

**P850** 				<RmngToBeSttldQty>

**P851** 					<FaceAmt>0</FaceAmt>

**P852** 				</RmngToBeSttldQty>

**P853** 				<SttlmAmt>

**P854** 					<Amt Ccy="EUR">0</Amt>

**P855** 				</SttlmAmt>

**P856** 				<TradDt>

**P857** 					<Dt>

**P858** 						<Dt>2025-09-23</Dt>

**P859** 					</Dt>

**P860** 				</TradDt>

**P861** 				<IntnddSttlmDt>

**P862** 					<Dt>

**P863** 						<Dt>2025-09-23</Dt>

**P864** 					</Dt>

**P865** 				</IntnddSttlmDt>

**P866** 				<FctvSttlmDt>

**P867** 					<Dt>2025-09-23</Dt>

**P868** 				</FctvSttlmDt>

**P869** 				<AckdStsTmStmp>2025-09-23T17:47:28.907861</AckdStsTmStmp>

**P870** 				<MtchdStsTmStmp>2025-09-23T17:47:28.919318</MtchdStsTmStmp>

**P871** 				<Prty>

**P872** 					<Nmrc>0004</Nmrc>

**P873** 				</Prty>

**P874** 				<DlvrgSttlmPties>

**P875** 					<Dpstry>

**P876** 						<Id>

**P877** 							<AnyBIC>PAAHPFP1000</AnyBIC>

**P878** 						</Id>

**P879** 					</Dpstry>

**P880** 					<Pty1>

**P881** 						<Id>

**P882** 							<AnyBIC>PAAHPFP1000</AnyBIC>

**P883** 						</Id>

**P884** 						<SfkpgAcct>

**P885** 							<Id>C5PFISSA362070</Id>

**P886** 						</SfkpgAcct>

**P887** 					</Pty1>

**P888** 				</DlvrgSttlmPties>

**P889** 				<RcvgSttlmPties>

**P890** 					<Dpstry>

**P891** 						<Id>

**P892** 							<AnyBIC>PAAHPFP1000</AnyBIC>

**P893** 						</Id>

**P894** 					</Dpstry>

**P895** 					<Pty1>

**P896** 						<Id>

**P897** 							<AnyBIC>PALLPFP1000</AnyBIC>

**P898** 						</Id>

**P899** 						<SfkpgAcct>

**P900** 							<Id>1000000123</Id>

**P901** 						</SfkpgAcct>

**P902** 					</Pty1>

**P903** 				</RcvgSttlmPties>

**P904** 				<MsgOrgtr>

**P905** 					<Id>

**P906** 						<Id>

**P907** 							<AnyBIC>PAAHPFP1000</AnyBIC>

**P908** 						</Id>

**P909** 					</Id>

**P910** 					<RspnsblPtyId>

**P911** 						<Id>

**P912** 							<AnyBIC>TCSOTCS0XXX</AnyBIC>

**P913** 						</Id>

**P914** 					</RspnsblPtyId>

**P915** 				</MsgOrgtr>

**P916** 				<CreDtTm>2025-09-23T17:47:26.064069</CreDtTm>

**P917** 			</TxDtls>

**P918** 		</Tx>

**P919** 	</Txs>

**P920** </SctiesSttlmTxQryRspn>

