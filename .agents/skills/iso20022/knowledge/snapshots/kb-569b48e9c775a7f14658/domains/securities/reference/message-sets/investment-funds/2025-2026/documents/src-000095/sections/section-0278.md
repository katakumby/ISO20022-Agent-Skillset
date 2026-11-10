---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Portfolio Transfer", "AccountHoldingInformation sese.018.001.10"]
content_origin: "source-transcription"
---

# AccountHoldingInformation sese.018.001.10

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Portfolio Transfer / AccountHoldingInformation sese.018.001.10.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4080** AccountHoldingInformation sese.018.001.10

**P4081** Description

**P4082** There are five assets:

**P4083** [1]	2,000 units of ISIN GB1111111111, Ethical Green Fund. The fund manager/transfer agent for this asset is TATAGB22.

**P4084** [2]	400 units of ISIN GB2222222222, Ethical Yellow Fund. The fund manager/transfer agent for this asset is FUNAGB22.

**P4085** [3]	300 units of ISIN GB3333333333, Ethical Red Fund. The fund manager/transfer agent for this asset is FUNBGB22.

**P4086** [4]	Cash assets not yet invested in the amount of GBP 3,000.

**P4087** [5]	Property (reference 'PropA01') with the value of GBP 725,000.

**P4088** The portfolio transfer reference provided in the AccountHoldingInformationRequest (sese.019) message, PORT-GB-001, is echoed back. 

**P4089** Message Instance 

**P4090** <AcctHldgInf>

**P4091** 		<MsgRef>

**P4092** 			<Id>EP-0001</Id>

**P4093** 			<CreDtTm>2026-03-04T09:15:00</CreDtTm>

**P4094** 		</MsgRef>

**P4095** 		<PmryIndvInvstr>

**P4096** 			<Nm>Brown</Nm>

**P4097** 			<GvnNm>Gethin</GvnNm>

**P4098** 			<IndvInvstrAdr>

**P4099** 				<AdrTp>HOME</AdrTp>

**P4100** 				<AdrLine>1 High Street</AdrLine>

**P4101** 				<PstCd>TW11 1RJ</PstCd>

**P4102** 				<TwnNm>Twickenham</TwnNm>

**P4103** 				<Ctry>GB</Ctry>

**P4104** 			</IndvInvstrAdr>

**P4105** 		</PmryIndvInvstr>

**P4106** 		<TrfrAcct>

**P4107** 			<Id>2000000</Id>

**P4108** 			<Svcr>

**P4109** 				<AnyBIC>BDAPGB22</AnyBIC>

**P4110** 			</Svcr>

**P4111** 		</TrfrAcct>

**P4112** 		<Trfee>

**P4113** 			<AnyBIC>PEFIGB22</AnyBIC>

**P4114** 		</Trfee>

**P4115** 		<PdctTrf>

**P4116** 			<TrfId>PORT-GB-001</TrfId>

**P4117** 			<FinInstrmAsstForTrf>	Repetition 1

**P4118** 				<Instrm>

**P4119** 					<Scty>

**P4120** 						<Id>

**P4121** 							<ISIN>GB1111111111</ISIN>

**P4122** 						</Id>

**P4123** 						<Nm>Ethical Green Fund </Nm>

**P4124** 					</Scty>

**P4125** 				</Instrm>

**P4126** 				<Qty>

**P4127** 					<Unit>2000</Unit>

**P4128** 				</Qty>

**P4129** 				<Trfr>

**P4130** 						<Svcr>

**P4131** 							<AnyBIC>TATAGB22</AnyBIC>

**P4132** 						</Svcr>

**P4133** 				</Trfr>

**P4134** 			</FinInstrmAsstForTrf>

**P4135** 			<FinInstrmAsstForTrf>		Repetition 2

**P4136** 				<Instrm>

**P4137** 					<Scty>

**P4138** 						<Id>

**P4139** 							<ISIN>GB2222222222</ISIN>

**P4140** 						</Id>

**P4141** 						<Nm>Ethical Yellow Fund </Nm>

**P4142** 					</Scty>

**P4143** 				</Instrm>

**P4144** 				<Qty>

**P4145** 					<Unit>400</Unit>

**P4146** 				</Qty>

**P4147** 				<Trfr>

**P4148** 						<Svcr>

**P4149** 							<AnyBIC>FUNAGB22</AnyBIC>

**P4150** 						</Svcr>

**P4151** 				</Trfr>

**P4152** 			</FinInstrmAsstForTrf>

**P4153** 			<FinInstrmAsstForTrf>		Repetition 3

**P4154** 				<Instrm>

**P4155** 					<Scty>

**P4156** 						<Id>

**P4157** 							<ISIN>GB3333333333</ISIN>

**P4158** 						</Id>

**P4159** 						<Nm>Ethical Red Fund </Nm>

**P4160** 					</Scty>

**P4161** 				</Instrm>

**P4162** 				<Qty>

**P4163** 					<Unit>300</Unit>

**P4164** 				</Qty>

**P4165** 				<Trfr>

**P4166** 						<Svcr>

**P4167** 							<AnyBIC>FUNBGB22</AnyBIC>

**P4168** 						</Svcr>

**P4169** 				</Trfr>

**P4170** 			</FinInstrmAsstForTrf>

**P4171** 			<FinInstrmAsstForTrf>		Repetition 4

**P4172** 				<Instrm>

**P4173** 					<CshAsst>

**P4174** 						<CshAsstTp>

**P4175** 							<Cd>CSH2</Cd>

**P4176** 						</CshAsstTp>

**P4177** 						<HldgCcy>GBP</HldgCcy>

**P4178** 					</CshAsst>

**P4179** 				</Instrm>

**P4180** 				<Qty>

**P4181** 					<CshAmt Ccy="GBP">3000</CshAmt>

**P4182** 				</Qty>

**P4183** 			</FinInstrmAsstForTrf>

**P4184** 			<FinInstrmAsstForTrf>		Repetition 5

**P4185** 				<Instrm>

**P4186** 					<OthrAsst>

**P4187** 						<OthrAsstTp>

**P4188** 							<Cd>PROP</Cd>

**P4189** 						</OthrAsstTp>

**P4190** 						<Id>PropA01</Id>

**P4191** 						<Desc>Edwardian Hall</Desc>

**P4192** 					</OthrAsst>

**P4193** 				</Instrm>

**P4194** 				<LatstValtn>

**P4195** 					<Dt>2020-03-01</Dt>

**P4196** 					<Amt Ccy="GBP">725000</Amt>

**P4197** 				</LatstValtn>

**P4198** 			</FinInstrmAsstForTrf>

**P4199** 		</PdctTrf>

**P4200** </AcctHldgInf>

