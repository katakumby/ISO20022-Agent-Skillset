---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Account Management ", "AccountOpeningInstruction acmt.001.001.08 – 1"]
content_origin: "source-transcription"
---

# AccountOpeningInstruction acmt.001.001.08 – 1

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Account Management  / AccountOpeningInstruction acmt.001.001.08 – 1.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P959** AccountOpeningInstruction acmt.001.001.08 – 1

**P960** Description

**P961** An AccountOpeningInstruction message is sent to an account servicer, by an institution requesting the opening of an account.

**P962** This AccountOpeningInstruction message instructs the account servicer to open a joint Euro Supplementary Retirement Scheme Account (SRSA). The account is to be opened in the name of Richard Lee, the primary owner, of French nationality, to whom the related correspondence is to be sent; Suzanne Plessey is a secondary owner, also of French nationality. The account is opened for investments in the Pension Equity Growth Fund family.

**P963** The account opening is requested with the following characteristics:

**P964** the statements are to be issued on a monthly basis,

**P965** any dividends from the investments are to be re-invested,

**P966** the tax is to be withheld at the source, 

**P967** a single owner only (the primary owner in this case) may authorise transactions on the account,

**P968** money laundering identification procedures have been carried out.

**P969** This message also instructs the opening of an investment plan in the Pension Equity Growth Europe B fund in bearer form, ISIN FR1234567890. The plan is defined as a yearly investment of EUR 523,20 starting on 2 February 2020. Any income is to be accumulated to the capital. 

**P970** The Euro amount to be invested on a yearly basis is to be paid through a direct debit transaction on IBAN account FR12345678987654321 at ASRVFRXX.

**P971** Message Instance

**P972** <AcctOpngInstr>

**P973** 	<MsgId>

**P974** 		<Id>123456-1</Id>

**P975** 		<CreDtTm>2020-01-06T09:30:30</CreDtTm>

**P976** 	</MsgId>

**P977** 	<InstrDtls>

**P978** 		<OpngTp>

**P979** 			<Cd>NEWA</Cd>

**P980** 		</OpngTp>

**P981** 	</InstrDtls>

**P982** 	<InvstmtAcct>

**P983** 		<Tp>

**P984** 			<Cd>SRSA</Cd>

**P985** 		</Tp>

**P986** 		<OwnrshTp>

**P987** 			<Cd>JOIN</Cd>

**P988** 		</OwnrshTp>

**P989** 		<StmtFrqcy>

**P990** 			<Cd>MNTH</Cd>

**P991** 		</StmtFrqcy>

**P992** 		<RefCcy>EUR</RefCcy>

**P993** 		<IncmPref>SECU</IncmPref>

**P994** 		<TaxWhldgMtd>WTHD</TaxWhldgMtd>

**P995** 		<ReqrdSgntriesNb>1</ReqrdSgntriesNb>

**P996** 		<FndFmlyNm>Pension Equity Growth</FndFmlyNm>

**P997** 	</InvstmtAcct>

**P998** 	<AcctPties>

**P999** 		<PrncplAcctPty>

**P1000** 			<PmryOwnr>

**P1001** 				<Pty>

**P1002** 					<IndvPrsn>

**P1003** 						<GvnNm>Richard</GvnNm>

**P1004** 						<Nm>Lee</Nm>

**P1005** 						<BirthDt>1961-05-09</BirthDt>

**P1006** 						<PstlAdr>

**P1007** 							<AdrTp>

**P1008** 								<Cd>HOME</Cd>

**P1009** 							</AdrTp>

**P1010** 							<MlngInd>true</MlngInd>

**P1011** 							<RegnAdrInd>true</RegnAdrInd>

**P1012** 							<AdrLine>Avenue Ariane 152</AdrLine>

**P1013** 							<PstCd>75005</PstCd>

**P1014** 							<TwnNm>Paris</TwnNm>

**P1015** 							<Ctry>FR</Ctry>

**P1016** 						</PstlAdr>

**P1017** 						<Ctznsh>

**P1018** 							<Ntlty>FR</Ntlty>

**P1019** 							<MnrInd>false</MnrInd>

**P1020** 						</Ctznsh>

**P1021** 					</IndvPrsn>

**P1022** 				</Pty>

**P1023** 				<MnyLndrgChck>

**P1024** 					<Cd>PASS</Cd>

**P1025** 				</MnyLndrgChck>

**P1026** 				<SgntryRghtInd>true</SgntryRghtInd>

**P1027** 			</PmryOwnr>

**P1028** 		</PrncplAcctPty>

**P1029** 		<ScndryOwnr>

**P1030** 			<Pty>

**P1031** 				<IndvPrsn>

**P1032** 					<GvnNm>Suzanne</GvnNm>

**P1033** 					<Nm>Plessey</Nm>

**P1034** 					<BirthDt>1962-05-16</BirthDt>

**P1035** 					<PstlAdr>

**P1036** 						<AdrTp>

**P1037** 							<Cd>HOME</Cd>

**P1038** 						</AdrTp>

**P1039** 						<MlngInd>true</MlngInd>

**P1040** 						<RegnAdrInd>true</RegnAdrInd>

**P1041** 						<AdrLine>Avenue Ariane 152</AdrLine>

**P1042** 						<PstCd>75005</PstCd>

**P1043** 						<TwnNm>Paris</TwnNm>

**P1044** 						<Ctry>FR</Ctry>

**P1045** 					</PstlAdr>

**P1046** 					<Ctznsh>

**P1047** 						<Ntlty>FR</Ntlty>

**P1048** 						<MnrInd>false</MnrInd>

**P1049** 					</Ctznsh>

**P1050** 				</IndvPrsn>

**P1051** 			</Pty>

**P1052** 			<MnyLndrgChck>

**P1053** 				<Cd>PASS</Cd>

**P1054** 			</MnyLndrgChck>

**P1055** 			<SgntryRghtInd>false</SgntryRghtInd>

**P1056** 		</ScndryOwnr>

**P1057** 	</AcctPties>

**P1058** 	<SvgsInvstmtPlan>

**P1059** 		<Frqcy>

**P1060** 			<Cd>YEAR</Cd>

**P1061** 		</Frqcy>

**P1062** 		<StartDt>2020-02-02</StartDt>

**P1063** 		<Qty>

**P1064** 			<Amt Ccy="EUR">523.20</Amt>

**P1065** 		</Qty>

**P1066** 		<SctyDtls>

**P1067** 			<Qty>

**P1068** 				<Pctg>100</Pctg>

**P1069** 			</Qty>

**P1070** 			<FinInstrm>

**P1071** 				<Id>

**P1072** 					<ISIN>FR1234567890</ISIN>

**P1073** 				</Id>

**P1074** 				<Nm>Pension Equity Growth Europe B</Nm>

**P1075** 				<SctiesForm>BEAR</SctiesForm>

**P1076** 				<DstrbtnPlcy>ACCU</DstrbtnPlcy>

**P1077** 			</FinInstrm>

**P1078** 		</SctyDtls>

**P1079** 	</SvgsInvstmtPlan>

**P1080** 	<CshSttlm>

**P1081** 		<OthrCshSttlmDtls>

**P1082** 			<SttlmCcy>EUR</SttlmCcy>

**P1083** 				<SvgsPlanPmtInstrm>

**P1084** 				<DrctDbtDtls>

**P1085** 					<DbtrAcct>

**P1086** 						<Id>

**P1087** 							<IBAN>FR12345678987654321</IBAN>

**P1088** 						</Id>

**P1089** 					</DbtrAcct>

**P1090** 					<DbtrAgt>

**P1091** 						<BICFI>ASRVFRXX</BICFI>

**P1092** 					</DbtrAgt>

**P1093** 				</DrctDbtDtls>

**P1094** 			</SvgsPlanPmtInstrm>

**P1095** 		</OthrCshSttlmDtls>

**P1096** 	</CshSttlm>

**P1097** </AcctOpngInstr>

