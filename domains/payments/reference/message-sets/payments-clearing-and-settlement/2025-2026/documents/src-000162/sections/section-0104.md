---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "FIToFIPaymentStatusRequest - pacs.028.001.07"]
content_origin: "source-transcription"
---

# FIToFIPaymentStatusRequest - pacs.028.001.07

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path Business Examples / FIToFIPaymentStatusRequest - pacs.028.001.07.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2506** FIToFIPaymentStatusRequest - pacs.028.001.07

**P2507** Description

**P2508** This example relates to the instruction message in section 7.6.1, a FIToFICustomerCreditTransfer message sent by BBBBUS33 to AAAAGB2L. No FIToFIPaymentStatusReport message was received yet, but BBBBUS33 wants to know the status of the instruction. BBBBUS33 therefore sends a FIToFIPaymentStatusRequest message to request a FIToFIPaymentStatusReport.

**P2509** Business Data 

**P2510** The FIToFIPaymentStatusRequest message, from Bank BBBBUS33 to Bank AAAAGB2L:

[T47 - complete table](../tables/tbl-0047.md)

**P2513** Message Instance

**P2514** <FIToFIPmtStsReq>

**P2515** 	<GrpHdr>

**P2516** 		<MsgId>BBBB/150929-CCT/JPY/456</MsgId>

**P2517** 		<CreDtTm>2015-09-28T16:06:00</CreDtTm>

**P2518** 		<InstgAgt>

**P2519** 			<FinInstnId>

**P2520** 				<BICFI>BBBBUS33</BICFI>

**P2521** 			</FinInstnId>

**P2522** 		</InstgAgt>

**P2523** 		<InstdAgt>

**P2524** 			<FinInstnId>

**P2525** 				<BICFI>AAAAGB2L</BICFI>

**P2526** 			</FinInstnId>

**P2527** 		</InstdAgt>

**P2528** 	</GrpHdr>

**P2529** 	<OrgnlGrpInf>

**P2530** 		<OrgnlMsgId>BBBB/150928-CCT/JPY/123</OrgnlMsgId>

**P2531** 		<OrgnlMsgNmId>pacs.008.001.12 </OrgnlMsgNmId>

**P2532** 		<OrgnlCreDtTm>2015-09-28T16:00:00</OrgnlCreDtTm>

**P2533** 	</OrgnlGrpInf>

**P2534** 	<TxInf>

**P2535** 		<StsReqId>BBBB/150928-CCT/JPY/456Request</StsReqId>

**P2536** 		<OrgnlInstrId>BBBB/150928-CCT/JPY/123/1</OrgnlInstrId>

**P2537** 		<OrgnlEndToEndId>ABC/4562/2015-09-08</OrgnlEndToEndId>

**P2538** 		<OrgnlTxId>BBBB/150928-CCT/JPY/123/1</OrgnlTxId>

**P2539** 		<AccptncDtTm>2015-09-28T15:45:00</AccptncDtTm>

**P2540** 		<OrgnlTxRef>

**P2541** 			<IntrBkSttlmAmt Ccy="JPY">10000000</IntrBkSttlmAmt>

**P2542** 			<IntrBkSttlmDt>2015-09-28</IntrBkSttlmDt>

**P2543** 			<PmtTpInf>

**P2544** 				<InstrPrty>NORM</InstrPrty>

**P2545** 			</PmtTpInf>

**P2546** 			<RmtInf>

**P2547** 				<Strd>

**P2548** 					<RfrdDocInf>

**P2549** 						<Tp>

**P2550** 							<CdOrPrtry>

**P2551** 								<Cd>CINV</Cd>

**P2552** 							</CdOrPrtry>

**P2553** 						</Tp>

**P2554** 						<Nb>4562</Nb>

**P2555** 						<RltdDt>

**P2556** 						<Tp>

**P2557** 							<Cd>INDA</Cd>

**P2558** 						</Tp>

**P2559** 						<Dt>2015-09-08</Dt>									

**P2560** 						</RltdDt>							

**P2561** 					</RfrdDocInf>

**P2562** 				</Strd>

**P2563** 			</RmtInf>

**P2564** 			<Dbtr>

**P2565** 				<Pty>

**P2566** 					<Nm>ABC Corporation</Nm>

**P2567** 					<PstlAdr>

**P2568** 						<StrtNm>Times Square</StrtNm>

**P2569** 						<BldgNb>7</BldgNb>

**P2570** 						<PstCd>NY 10036</PstCd>

**P2571** 						<TwnNm>New York</TwnNm>

**P2572** 						<Ctry>US</Ctry>

**P2573** 					</PstlAdr>

**P2574** 				</Pty>

**P2575** 			</Dbtr>

**P2576** 			<DbtrAcct>

**P2577** 				<Id>

**P2578** 					<Othr>

**P2579** 						<Id>00125574999</Id>

**P2580** 					</Othr>

**P2581** 				</Id>

**P2582** 			</DbtrAcct>

**P2583** 			<DbtrAgt>

**P2584** 				<FinInstnId>

**P2585** 					<BICFI>BBBBUS33</BICFI>

**P2586** 				</FinInstnId>

**P2587** 			</DbtrAgt>

**P2588** 			<CdtrAgt>

**P2589** 				<FinInstnId>

**P2590** 					<BICFI>AAAAGB2L</BICFI>

**P2591** 				</FinInstnId>

**P2592** 			</CdtrAgt>

**P2593** 			<Cdtr>

**P2594** 				<Pty>

**P2595** 					<Nm>DEF Electronics</Nm>

**P2596** 					<PstlAdr>

**P2597** 						<StrtNm>Mark Lane</StrtNm>

**P2598** 						<BldgNb>55</BldgNb>

**P2599** 						<PstCd>EC3R7NE</PstCd>

**P2600** 						<TwnNm>London</TwnNm>

**P2601** 						<Ctry>GB</Ctry>

**P2602** 						<AdrLine>Corn Exchange 5th Floor</AdrLine>

**P2603** 					</PstlAdr>

**P2604** 				</Pty>

**P2605** 			</Cdtr>

**P2606** 			<CdtrAcct>

**P2607** 				<Id>

**P2608** 					<Othr>

**P2609** 						<Id>23683707994215</Id>

**P2610** 					</Othr>

**P2611** 				</Id>

**P2612** 			</CdtrAcct>

**P2613** 		</OrgnlTxRef>

**P2614** 	</TxInf>

**P2615** </FIToFIPmtStsReq>

