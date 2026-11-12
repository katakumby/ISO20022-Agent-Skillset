---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Portfolio Transfer", "PortfolioTransferInstruction sese.012.001.12"]
content_origin: "source-transcription"
---

# PortfolioTransferInstruction sese.012.001.12

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Portfolio Transfer / PortfolioTransferInstruction sese.012.001.12.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4201** PortfolioTransferInstruction sese.012.001.12

**P4202** Description

**P4203** A PortfolioTransferInstruction message is sent by the new plan manager (transferee/acquiring party), PEFIGB22, to the old plan manager (transferor/ceding party), BDAPGB22. 

**P4204** The PortfolioTransferInstruction message is an instruction to transfer the client's (Mr. Gethin Brown) individual assets. The transfer of the five assets are instructed in the following way:

**P4205** Asset 1

**P4206** ISIN GB1111111111, Ethical Green Fund, is to be transferred as units (SECU). The fund manager/transfer agent for this asset is TATAGB22. The units are to be delivered to the account of PEFIGB22 (transferee), account 444444, at TATAGB22.

**P4207** The reference that PEFIGB22 assigns to the transfer of these units is PEFI-TI-U001.

**P4208** Asset 2

**P4209** ISIN GB2222222222, Ethical Yellow Fund, is to be redeemed and transferred as cash (CASH). The fund manager/transfer agent for this asset is FUNAGB22.

**P4210** Asset 3

**P4211** ISIN GB3333333333, Ethical Red Fund, is to be converted (CONV) to ISIN GB4444444444, Ethical Blue Fund, and the units transferred. The fund manager/transfer agent for this asset is FUNBGB22. The units are to be delivered to the account of PEFIGB22 (transferee), account 555555, at FUNBGB22.

**P4212** The reference that PEFIGB22 assigns to the transfer of these units is PEFI-TI-U002.

**P4213** Asset 4

**P4214** The GBP 3000 cash asset (CSH1) is to be transferred as cash (CASH). 

**P4215** Asset 5

**P4216** The property, reference ' PropA01', is to be transferred in specie (SECU). This transfer is subsequently covered manually and is not in scope of the ISO 20022 transfer messaging.

**P4217** Quantity of Units

**P4218** The quantity of units element is optional in the PortfolioTransferInstruction (sese.012) message. It is unlikely that the transferee will echo back the quantity of units provided in the AccountHoldingInformation (sese.018) message, since the number of units could change between the time the AccountHoldingInformation (sese.018) message is received and the PortfolioTransferInstruction (sese.012) message is sent.

**P4219** Cash Payment Information

**P4220** The cash for both the redemption of asset 2 and the cash asset, asset 4, is to be paid to the account of PEFIGB22 at BARCGB22. The payment reference specified is PORT-GB-001-PAYM. The cash is to be paid to IBAN GB85324906366027 at BARCGB22 (sort code SC600501). The subsequent cash payment instruction/s are not shown.

**P4221** Message Instance

**P4222** <PrtflTrfInstr>

**P4223** 		<MsgRef>

**P4224** 			<Id>IP-0002</Id>

**P4225** 			<CreDtTm>2026-03-05T10:30:00</CreDtTm>

**P4226** 		</MsgRef>

**P4227** 		<PmryIndvInvstr>

**P4228** 			<Nm>Brown</Nm>

**P4229** 			<GvnNm>Gethin</GvnNm>

**P4230** 			<IndvInvstrAdr>

**P4231** 				<AdrTp>HOME</AdrTp>

**P4232** 				<AdrLine>1 High Street</AdrLine>

**P4233** 				<PstCd>TW11 1RJ</PstCd>

**P4234** 				<TwnNm>Twickenham</TwnNm>

**P4235** 				<Ctry>GB</Ctry>

**P4236** 			</IndvInvstrAdr>

**P4237** 		</PmryIndvInvstr>

**P4238** 		<TrfrAcct>

**P4239** 			<Id>2000000</Id>

**P4240** 			<Svcr>

**P4241** 				<AnyBIC>BDAPGB22</AnyBIC>

**P4242** 			</Svcr>

**P4243** 		</TrfrAcct>

**P4244** 		<Trfee>

**P4245** 			<AnyBIC>PEFIGB22</AnyBIC>

**P4246** 		</Trfee>

**P4247** 		<PdctTrf>

**P4248** 			<TrfId>PORT-GB-001</TrfId>

**P4249** 			<PmtDtls>

**P4250** 				<Ref>PORT-GB-001-PAYM</Ref>

**P4251** 					<CdtTrfDtls>

**P4252** 						<CdtrAgt>

**P4253** 							<BICFI>BARCGB22</BICFI>

**P4254** 							<ClrSysMmbId>

**P4255** 								<GBSC>SC600501</GBSC>

**P4256** 							</ClrSysMmbId>

**P4257** 						</CdtrAgt>

**P4258** 						<CdtrAcct>

**P4259** 							<IBAN>GB85324906366027</IBAN>

**P4260** 						</CdtrAcct>

**P4261** 					</CdtTrfDtls>

**P4262** 			</PmtDtls>

**P4263** 			<FinInstrmAsstForTrf>		Repetition 1

**P4264** 				<Instrm>

**P4265** 					<Scty>

**P4266** 						<Id>

**P4267** 							<ISIN>GB1111111111</ISIN>

**P4268** 						</Id>

**P4269** 						<Nm>Ethical Green Fund</Nm>

**P4270** 					</Scty>

**P4271** 				</Instrm>

**P4272** 				<TrfTp>

**P4273** 					<Cd>SECU</Cd>

**P4274** 				</TrfTp>

**P4275** 				<ClntRef>

**P4276** 					<Ref>PEFI-TI-U001</Ref>

**P4277** 				</ClntRef>

**P4278** 				<TrfeeAcct>

**P4279** 					<OwnrId>

**P4280** 						<AnyBIC>PEFILULL</AnyBIC>

**P4281** 					</OwnrId>

**P4282** 					<AcctId>444444</AcctId>

**P4283** 					<Svcr>

**P4284** 						<AnyBIC>TATAGB22</AnyBIC>

**P4285** 					</Svcr>

**P4286** 				</TrfeeAcct>

**P4287** 			</FinInstrmAsstForTrf>

**P4288** 			<FinInstrmAsstForTrf>		Repetition 2

**P4289** 				<Instrm>

**P4290** 					<Scty>

**P4291** 						<Id>

**P4292** 							<ISIN>GB2222222222</ISIN>

**P4293** 						</Id>

**P4294** 						<Nm>Ethical Yellow Fund</Nm>

**P4295** 					</Scty>

**P4296** 				</Instrm>

**P4297** 				<TrfTp>

**P4298** 					<Cd>CASH</Cd>

**P4299** 				</TrfTp>

**P4300** 			</FinInstrmAsstForTrf>

**P4301** 			<FinInstrmAsstForTrf>	Repetition 3

**P4302** 				<Instrm>

**P4303** 					<Scty>

**P4304** 						<Id>

**P4305** 							<ISIN>GB3333333333</ISIN>

**P4306** 						</Id>

**P4307** 						<Nm>Ethical Red Fund</Nm>

**P4308** 					</Scty>

**P4309** 				</Instrm>

**P4310** 				<TrfTp>

**P4311** 					<Cd>CONV</Cd>

**P4312** 				</TrfTp>

**P4313** 				<Convs>

**P4314** 					<TrgtScty>

**P4315** 						<Id>

**P4316** 							<ISIN>GB4444444444</ISIN>

**P4317** 						</Id>

**P4318** 						<Nm>Ethical Blue Fund</Nm>

**P4319** 					</TrgtScty>

**P4320** 				</Convs>

**P4321** 				<ClntRef>

**P4322** 					<Ref>PEFI-TI-U002</Ref>

**P4323** 				</ClntRef>

**P4324** 				<TrfeeAcct>

**P4325** 					<OwnrId>

**P4326** 						<AnyBIC>PEFIGB22</AnyBIC>

**P4327** 					</OwnrId>

**P4328** 					<AcctId>55555</AcctId>

**P4329** 					<Svcr>

**P4330** 						<AnyBIC>FUNBGB22</AnyBIC>

**P4331** 					</Svcr>

**P4332** 				</TrfeeAcct>

**P4333** 			</FinInstrmAsstForTrf>

**P4334** 			<FinInstrmAsstForTrf>		Repetition 4

**P4335** 				<Instrm>

**P4336** 					<CshAsst>

**P4337** 						<CshAsstTp>

**P4338** 							<Cd>CSH1</Cd>

**P4339** 						</CshAsstTp>

**P4340** 						<HldgCcy>GBP</HldgCcy>

**P4341** 					</CshAsst>

**P4342** 				</Instrm>

**P4343** 				<TrfTp>

**P4344** 					<Cd>CASH</Cd>

**P4345** 				</TrfTp>

**P4346** 			</FinInstrmAsstForTrf>

**P4347** 			<FinInstrmAsstForTrf>		Repetition 5

**P4348** 				<Instrm>

**P4349** 					<OthrAsst>

**P4350** 						<OthrAsstTp>

**P4351** 							<Cd>PROP</Cd>

**P4352** 						</OthrAsstTp>

**P4353** 						<Id>PropA01</Id>

**P4354** 						<Desc>Edwardian Hall</Desc>

**P4355** 					</OthrAsst>

**P4356** 				</Instrm>

**P4357** 				<TrfTp>

**P4358** 					<Cd>SECU</Cd>

**P4359** 				</TrfTp>

**P4360** 			</FinInstrmAsstForTrf>

**P4361** 		</PdctTrf>

**P4362** </PrtflTrfInstr>

