---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["Business Examples", "Securities Account Position Response (semt.040)"]
content_origin: "source-transcription"
---

# Securities Account Position Response (semt.040)

Source: [src-000374](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Locator: heading path Business Examples / Securities Account Position Response (semt.040).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P922** Securities Account Position Response (semt.040)

**P923** Description

**P924** In this example T2S sends a Securities Account Position Response containing 3 restriction references matching the query criteria specified in the query with reference “MSG700”, which is requesting the current day positions related to the Restriction Type “BLK1” within securities account “1000000123”. The securities positions returned in respond to the query are the current day positions at 09:30:47 with the following details:

**P925** Securities account “1000000123” with 4000 “ISIN00000002” blocked (not available) at BLK1.

**P926** – 1000 units with restriction reference 98586776475.

**P927** – 1000 units with restriction reference 98745787450.

**P928** – 2000 units with restriction reference 1234767634.

**P929** Message Instance

**P931** <SctiesAcctPosRspn>

**P932** 		<Pgntn>

**P933** 			<PgNb>1</PgNb>

**P934** 			<LastPgInd>true</LastPgInd>

**P935** 		</Pgntn>

**P936** 		<RptGnlDtls>

**P937** 			<QryRef>MSG700</QryRef>

**P938** 			<HstrcData>false</HstrcData>

**P939** 			<ActvtyInd>true</ActvtyInd>

**P940** 			<SubAcctInd>false</SubAcctInd>

**P941** 		</RptGnlDtls>

**P942** 		<AcctOwnr>

**P943** 			<Id>

**P944** 				<AnyBIC>PRTAFRPPXXX</AnyBIC>

**P945** 			</Id>

**P946** 		</AcctOwnr>

**P947** 		<AcctSvcr>

**P948** 			<Id>

**P949** 				<AnyBIC>CSDBBIC2XXX</AnyBIC>

**P950** 			</Id>

**P951** 		</AcctSvcr>

**P952** 		<Bals>

**P953** 			<SfkpgAcct>

**P954** 				<Id>1000000123</Id>

**P955** 			</SfkpgAcct>

**P956** 			<BalForAcct>

**P957** 				<BalDt>

**P958** 					<DtTm>2025-09-12T09:30:47.000</DtTm>

**P959** 				</BalDt>

**P960** 				<FinInstrmId>

**P961** 					<ISIN>ISIN00000002</ISIN>

**P962** 				</FinInstrmId>

**P963** 				<NotAvlblBal>

**P964** 					<Qty>

**P965** 						<Unit>4000</Unit>

**P966** 					</Qty>

**P967** 				</NotAvlblBal>

**P968** 				<BalBrkdwn>

**P969** 					<SubBalTp>

**P970** 						<Prtry>

**P971** 							<Id>BLCK</Id>

**P972** 							<Issr>T2S</Issr>

**P973** 							<SchmeNm>RPT</SchmeNm>

**P974** 						</Prtry>

**P975** 					</SubBalTp>

**P976** 					<Qty>

**P977** 						<Qty>

**P978** 							<Qty>

**P979** 								<Unit>4000</Unit>

**P980** 							</Qty>

**P981** 						</Qty>

**P982** 					</Qty>

**P983** 					<AddtlBalBrkdwnDtls>

**P984** 						<SubBalTp>

**P985** 							<Prtry>

**P986** 								<Id>BLK1</Id>

**P987** 								<Issr>T2S</Issr>

**P988** 								<SchmeNm>RT</SchmeNm>

**P989** 							</Prtry>

**P990** 						</SubBalTp>

**P991** 						<Qty>

**P992** 							<Qty>

**P993** 								<Qty>

**P994** 									<Unit>4000</Unit>

**P995** 								</Qty>

**P996** 							</Qty>

**P997** 						</Qty>

**P998** 						<SubBalAddtlDtls>Blocked restriction type 1</SubBalAddtlDtls>

**P999** 						<QtyBrkdwn>

**P1000** 							<LotNb>

**P1001** 								<Id>98586776475</Id>

**P1002** 							</LotNb>

**P1003** 							<LotQty>

**P1004** 								<Qty>

**P1005** 									<Qty>

**P1006** 										<Qty>

**P1007** 											<Unit>1000</Unit>

**P1008** 										</Qty>

**P1009** 									</Qty>

**P1010** 								</Qty>

**P1011** 							</LotQty>

**P1012** 						</QtyBrkdwn>

**P1013** 						<QtyBrkdwn>

**P1014** 							<LotNb>

**P1015** 								<Id>98745787450</Id>

**P1016** 							</LotNb>

**P1017** 							<LotQty>

**P1018** 								<Qty>

**P1019** 									<Qty>

**P1020** 										<Qty>

**P1021** 											<Unit>1000</Unit>

**P1022** 										</Qty>

**P1023** 									</Qty>

**P1024** 								</Qty>

**P1025** 							</LotQty>

**P1026** 						</QtyBrkdwn>

**P1027** 						<QtyBrkdwn>

**P1028** 							<LotNb>

**P1029** 								<Id>1234767634</Id>

**P1030** 							</LotNb>

**P1031** 							<LotQty>

**P1032** 								<Qty>

**P1033** 									<Qty>

**P1034** 										<Qty>

**P1035** 											<Unit>2000</Unit>

**P1036** 										</Qty>

**P1037** 									</Qty>

**P1038** 								</Qty>

**P1039** 							</LotQty>

**P1040** 						</QtyBrkdwn>

**P1041** 					</AddtlBalBrkdwnDtls>

**P1042** 				</BalBrkdwn>

**P1043** 			</BalForAcct>

**P1044** 		</Bals>

**P1045** 	</SctiesAcctPosRspn>

**P1046**   


