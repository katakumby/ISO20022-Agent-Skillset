---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Portfolio Transfer", "AccountHoldingInformationRequest sese.019.001.09"]
content_origin: "source-transcription"
---

# AccountHoldingInformationRequest sese.019.001.09

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Portfolio Transfer / AccountHoldingInformationRequest sese.019.001.09.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4036** AccountHoldingInformationRequest sese.019.001.09

**P4037** Description

**P4038** An AccountHoldingInformationRequest is sent by the new plan manager (transferee/acquiring party), PEFIGB22, to the old plan manager (transferor/ceding party), BDAPGB22, to request information about a stocks and shares ISA (EQUI) managed on behalf of the client, Gethin Brown. The client's account at the old plan manager is 2000000.The reference for the intended portfolio transfer is PORT-GB-001.

**P4039** Message Instance 

**P4040** <AcctHldgInfReq>

**P4041** 		<MsgRef>

**P4042** 			<Id>IP-0001</Id>

**P4043** 			<CreDtTm>2026-03-01T09:15:00</CreDtTm>

**P4044** 		</MsgRef>

**P4045** 		<PmryIndvInvstr>

**P4046** 			<Nm>Brown</Nm>

**P4047** 			<GvnNm>Gethin</GvnNm>

**P4048** 			<IndvInvstrAdr>

**P4049** 				<AdrTp>HOME</AdrTp>

**P4050** 				<AdrLine>1 High Street</AdrLine>

**P4051** 				<PstCd>TW11 1RJ</PstCd>

**P4052** 				<TwnNm>Twickenham</TwnNm>

**P4053** 				<Ctry>GB</Ctry>

**P4054** 			</IndvInvstrAdr>

**P4055** 		</PmryIndvInvstr>

**P4056** 		<TrfrAcct>

**P4057** 			<Id>2000000</Id>

**P4058** 			<Svcr>

**P4059** 				<AnyBIC>BDAPGB22</AnyBIC>

**P4060** 			</Svcr>

**P4061** 		</TrfrAcct>

**P4062** 		<Trfee>

**P4063** 			<AnyBIC>PEFIGB22</AnyBIC>

**P4064** 		</Trfee>

**P4065** 		<PdctTrf>

**P4066** 			<TrfId>PORT-GB-001</TrfId>

**P4067** 			<Prtfl>

**P4068** 				<TaxEffcntPdct>

**P4069** 					<TaxEffcntPdctTp>

**P4070** 						<Cd>EQUI</Cd>

**P4071** 					</TaxEffcntPdctTp>

**P4072** 					<CurYr>true</CurYr>

**P4073** 					<PrvsYrs>

**P4074** 						<AllPrvsYrs>ALL</AllPrvsYrs>

**P4075** 					</PrvsYrs>

**P4076** 				</TaxEffcntPdct>

**P4077** 			</Prtfl>

**P4078** 		</PdctTrf>

**P4079** </AcctHldgInfReq>

