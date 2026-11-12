---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Portfolio Transfer", "PortfolioTransferConfirmation sese.013.001.12"]
content_origin: "source-transcription"
---

# PortfolioTransferConfirmation sese.013.001.12

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Portfolio Transfer / PortfolioTransferConfirmation sese.013.001.12.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4363** PortfolioTransferConfirmation sese.013.001.12

**P4364** Description

**P4365** A PortfolioTransferConfirmation message is sent by the old plan manager (transferor/ceding party), BDAPGB22 to the new plan manager (transferee/acquiring party), PEFIGB2, to confirm the intent to transfer the client's (Mr. Gethin Brown) individual assets.

**P4366** BDAPGB22 echoes back the MasterReference element, PORT-GB-001, from the PortfolioTransferInstruction (sese.012) message. 

**P4367** BDAPGB22 adds its own reference for the portfolio transfer, EP-PORT-GB-001-224.

**P4368** Asset 1

**P4369** ISIN GB1111111111, Ethical Green Fund, is to be transferred as units (SECU). The fund manager/transfer agent for this asset is TATAGB22. The units are to be delivered to the account of PEFIGB22 (transferee), account 444444, at TATAGB22. 

**P4370** The reference that PEFIGB22 assigned to the transfer of these units, PEFI-TI-U001, is echoed back from the PortfolioTransferInstruction (sese.012) message.

**P4371** The quantity of units is 2,000. 

**P4372** The units are to be delivered from the account of BDAPGB22, account 999999 at TATAGB22.

**P4373** The original cost of the asset is GBP 20,000.

**P4374** Asset 2

**P4375** ISIN GB2222222222, Ethical Yellow Fund, is to be redeemed and transferred as cash (CASH). The fund manager/transfer agent for this asset is FUNAGB22.

**P4376** The quantity of units is 400. 

**P4377** The total book value of the asset is GBP 8,000.

**P4378** Asset 3

**P4379** ISIN GB3333333333, Ethical Red Fund, is to be converted (CONV) to ISIN GB4444444444, Ethical Blue Fund, and the units transferred. The fund manager/transfer agent for this asset is FUNBGB22. The units are to be delivered to the account of PEFIGB22 (transferee), account 555555, at FUNBGB22.

**P4380** The reference that PEFIGB22 assigned to the transfer of these units, PEFI-TI-U002 is echoed back is echoed back from the PortfolioTransferInstruction (sese.012) message.

**P4381** The quantity of units is 300. 

**P4382** The units are to be delivered from the account of BDAPGB22, account 888888 at FUNBGB22.

**P4383** The original cost of the asset is GBP 6,000.

**P4384** Asset 4

**P4385** The GBP 3,000 cash asset (CSH1) is to be transferred as cash (CASH). 

**P4386** Asset 5

**P4387** The property, reference ' PropA01', is to be transferred in specie (SECU). This transfer is subsequently covered manually and is not in scope of the ISO transfer messaging). 

**P4388** The latest valuation of the asset, on 1 March 2020, is GBP 725,200.

**P4389** Cash Payment Information

**P4390** The cash for both the redemption of asset 2 and the cash asset, assert 4, is to be paid to the account of PEFIGB22 and BARCGB22. The payment information from the PortfolioTransferInstruction (sese.012) message is echoed back:

**P4391** The payment reference quoted is PORT-GB-001-PAYM. 

**P4392** The cash is to be paid to IBAN GB85324906366027 at BARCGB22 (sort code SC600501). 

**P4393** Message Instance

**P4394** <PrtflTrfConf>

**P4395** 		<MsgRef>

**P4396** 			<Id>EP-0002</Id>

**P4397** 			<CreDtTm>2026-03-06T16:35:00</CreDtTm>

**P4398** 		</MsgRef>

**P4399** 		<PmryIndvInvstr>

**P4400** 			<Nm>Brown</Nm>

**P4401** 			<GvnNm>Gethin</GvnNm>

**P4402** 			<IndvInvstrAdr>

**P4403** 				<AdrTp>HOME</AdrTp>

**P4404** 				<AdrLine>1 High Street</AdrLine>

**P4405** 				<PstCd>TW11 1RJ</PstCd>

**P4406** 				<TwnNm>Twickenham</TwnNm>

**P4407** 				<Ctry>GB</Ctry>

**P4408** 			</IndvInvstrAdr>

**P4409** 		</PmryIndvInvstr>

**P4410** 		<TrfrAcct>

**P4411** 			<Id>2000000</Id>

**P4412** 			<Svcr>

**P4413** 				<AnyBIC>BDAPGB22</AnyBIC>

**P4414** 			</Svcr>

**P4415** 		</TrfrAcct>

**P4416** 		<Trfee>

**P4417** 			<AnyBIC>PEFIGB22</AnyBIC>

**P4418** 		</Trfee>

**P4419** 		<PdctTrf>

**P4420** 			<TrfInstrRef>PORT-GB-001</TrfInstrRef>

**P4421** 			<TrfConfId>EP-PORT-GB-001-224</TrfConfId>

**P4422** 			<PmtDtls>

**P4423** 				<Ref>PORT-GB-001-PAYM</Ref>

**P4424** 					<CdtTrfDtls>

**P4425** 						<CdtrAgt>

**P4426** 							<BICFI>BARCGB22</BICFI>

**P4427** 							<ClrSysMmbId>

**P4428** 								<GBSC>SC600501</GBSC>

**P4429** 							</ClrSysMmbId>

**P4430** 						</CdtrAgt>

**P4431** 						<CdtrAcct>

**P4432** 							<IBAN>GB85324906366027</IBAN>

**P4433** 						</CdtrAcct>

**P4434** 					</CdtTrfDtls>

**P4435** 			</PmtDtls>

**P4436** 			<FinInstrmAsstForTrf> 		Repetition 1

**P4437** 				<Instrm>

**P4438** 					<Scty>

**P4439** 							<Id>

**P4440** 								<ISIN>GB1111111111</ISIN>

**P4441** 							</Id>

**P4442** 							<Nm>Ethical Green Fund</Nm>

**P4443** 						</Scty>

**P4444** 					</Instrm>

**P4445** 				<Qty>

**P4446** 					<Unit>2000</Unit>

**P4447** 				</Qty>

**P4448** 				<TrfTp>

**P4449** 					<Cd>SECU</Cd>

**P4450** 				</TrfTp>

**P4451** 				<ClntRef>

**P4452** 					<Ref>PEFI-TI-U001</Ref>

**P4453** 				</ClntRef>

**P4454** 				<OrgnlCost Ccy="GBP">20000</OrgnlCost>

**P4455** 				<TrfeeAcct>

**P4456** 					<OwnrId>

**P4457** 						<AnyBIC>PEFILULL</AnyBIC>

**P4458** 					</OwnrId>

**P4459** 					<AcctId>444444</AcctId>

**P4460** 					<Svcr>

**P4461** 						<AnyBIC>TATAGB22</AnyBIC>

**P4462** 					</Svcr>

**P4463** 				</TrfeeAcct>

**P4464** 				<Trfr>

**P4465** 					<OwnrId>

**P4466** 						<AnyBIC>BDAPGB22</AnyBIC>

**P4467** 					</OwnrId>

**P4468** 					<AcctId>999999</AcctId>

**P4469** 					<Svcr>

**P4470** 						<AnyBIC>TATAGB22</AnyBIC>

**P4471** 					</Svcr>

**P4472** 				</Trfr>

**P4473** 			</FinInstrmAsstForTrf>

**P4474** 			<FinInstrmAsstForTrf> 		Repetition 2

**P4475** 				<Instrm>

**P4476** 					<Scty>

**P4477** 						<Id>

**P4478** 							<ISIN>GB2222222222</ISIN>

**P4479** 						</Id>

**P4480** 						<Nm>Ethical Yellow Fund</Nm>

**P4481** 					</Scty>

**P4482** 				</Instrm>

**P4483** 				<Qty>

**P4484** 					<Unit>400</Unit>

**P4485** 				</Qty>

**P4486** 				<TrfTp>

**P4487** 					<Cd>CASH</Cd>

**P4488** 				</TrfTp>

**P4489** 				<TtlBookVal>

**P4490** 					<Amt Ccy="GBP">8000</Amt>

**P4491** 				</TtlBookVal>

**P4492** 			</FinInstrmAsstForTrf>

**P4493** 			<FinInstrmAsstForTrf> 		Repetition 3

**P4494** 				<Instrm>

**P4495** 					<Scty>

**P4496** 						<Id>

**P4497** 							<ISIN>GB3333333333</ISIN>

**P4498** 						</Id>

**P4499** 						<Nm>Ethical Red Fund</Nm>

**P4500** 					</Scty>

**P4501** 				</Instrm>

**P4502** 				<Qty>

**P4503** 					<Unit>300</Unit>

**P4504** 				</Qty>

**P4505** 				<TrfTp>

**P4506** 					<Cd>CONV</Cd>

**P4507** 				</TrfTp>

**P4508** 				<Convs>

**P4509** 					<TrgtScty>

**P4510** 						<Id>

**P4511** 							<ISIN>GB4444444444</ISIN>

**P4512** 						</Id>

**P4513** 						<Nm>Ethical Blue Fund</Nm>

**P4514** 					</TrgtScty>

**P4515** 				</Convs>

**P4516** 				<ClntRef>

**P4517** 					<Ref>PEFI-TI-U002</Ref>

**P4518** 				</ClntRef>

**P4519** 				<OrgnlCost Ccy="GBP">6000</OrgnlCost>

**P4520** 				<TrfeeAcct>

**P4521** 					<OwnrId>

**P4522** 						<AnyBIC>PEFIGB22</AnyBIC>

**P4523** 					</OwnrId>

**P4524** 					<AcctId>55555</AcctId>

**P4525** 					<Svcr>

**P4526** 						<AnyBIC>FUNBGB22</AnyBIC>

**P4527** 					</Svcr>

**P4528** 				</TrfeeAcct>

**P4529** 				<Trfr>

**P4530** 					<OwnrId>

**P4531** 						<AnyBIC>BDAPGB22</AnyBIC>

**P4532** 					</OwnrId>

**P4533** 					<AcctId>888888</AcctId>

**P4534** 					<Svcr>

**P4535** 						<AnyBIC>FUNBGB22</AnyBIC>

**P4536** 					</Svcr>

**P4537** 				</Trfr>

**P4538** 			</FinInstrmAsstForTrf>

**P4539** 			<FinInstrmAsstForTrf> 	Repetition 4

**P4540** 				<Instrm>

**P4541** 					<CshAsst>

**P4542** 							<CshAsstTp>

**P4543** 								<Cd>CSH1</Cd>

**P4544** 							</CshAsstTp>

**P4545** 							<HldgCcy>GBP</HldgCcy>

**P4546** 					</CshAsst>

**P4547** 				</Instrm>

**P4548** 					<Qty>

**P4549** 						<CshAmt Ccy="GBP">3000</CshAmt>

**P4550** 					</Qty>

**P4551** 					<TrfTp>

**P4552** 						<Cd>CASH</Cd>

**P4553** 					</TrfTp>

**P4554** 			</FinInstrmAsstForTrf>

**P4555** 			<FinInstrmAsstForTrf> 		Repetition 5

**P4556** 				<Instrm>

**P4557** 					<OthrAsst>

**P4558** 						<OthrAsstTp>

**P4559** 							<Cd>PROP</Cd>

**P4560** 						</OthrAsstTp>

**P4561** 						<Id>PropA01</Id>

**P4562** 						<Desc>Edwardian Hall</Desc>

**P4563** 					</OthrAsst>

**P4564** 				</Instrm>

**P4565** 				<TrfTp>

**P4566** 					<Cd>SECU</Cd>

**P4567** 				</TrfTp>

**P4568** 				<LatstValtn>

**P4569** 					<Dt>2020-03-01</Dt>

**P4570** 					<Amt Ccy="GBP">750200</Amt>

**P4571** 				</LatstValtn>

**P4572** 		</FinInstrmAsstForTrf>

**P4573** 	</PdctTrf>

**P4574** </PrtflTrfConf>

