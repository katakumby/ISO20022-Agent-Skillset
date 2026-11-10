---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["Business Examples", "Billing", "camt.077 Invoice"]
content_origin: "source-transcription"
---

# camt.077 Invoice

Source: [src-000347](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`. Locator: heading path Business Examples / Billing / camt.077 Invoice.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P209** camt.077 Invoice

**P210** Description

**P211** The Invoice message provides customer with the legal invoice.

**P212** Message Instance

**P213** <BllgRpt>

**P214**         <MsgHdr>

**P215**             <MsgId>NONREF</MsgId>

**P216**             <ReqTp>

**P217**                 <Prtry>

**P218**                     <Id>INVC</Id>

**P219**                 </Prtry>

**P220**             </ReqTp>

**P221**         </MsgHdr>

**P222**         <BllgRptOrErr>

**P223**             <BllgRpt>

**P224**                 <RgltryData>

**P225**                     <Invcr>

**P226**                         <Nm>Invoicername</Nm>

**P227**                         <PstlAdr>

**P228**                             <StrtNm>Street</StrtNm>

**P229**                             <BldgNb>Buildingnumber</BldgNb>

**P230**                             <PstCd>Postcode</PstCd>

**P231**                             <TwnNm>Town</TwnNm>

**P232**                             <CtrySubDvsn>CountrySubDivision</CtrySubDvsn>

**P233**                             <Ctry>IT</Ctry>

**P234**                         </PstlAdr>

**P235**                         <CtctDtls>

**P236**                             <PhneNb>+39-123456789</PhneNb>

**P237**                             <EmailAdr>Invoicer(at)bill.eu</EmailAdr>

**P238**                         </CtctDtls>

**P239**                     </Invcr>

**P240**                     <Invcee>

**P241**                         <Nm>Invoiceename</Nm>

**P242**                         <PstlAdr>

**P243**                             <StrtNm>Street</StrtNm>

**P244**                             <BldgNb>Buildingnumber</BldgNb>

**P245**                             <PstCd>Postcode</PstCd>

**P246**                             <TwnNm>Town</TwnNm>

**P247**                             <CtrySubDvsn>CountrySubDivision</CtrySubDvsn>

**P248**                             <Ctry>IT</Ctry>

**P249**                         </PstlAdr>

**P250**                     </Invcee>

**P251**                     <InvcLglStmt>LEGAL STATEMENT</InvcLglStmt>

**P252**                     <PmtMtd>

**P253**                         <Prtry>PAYMENT METHOD</Prtry>

**P254**                     </PmtMtd>

**P255**                 </RgltryData>

**P256**                 <Svc>

**P257**                     <SysId>

**P258**                         <MktInfrstrctrId>

**P259**                             <Prtry>T2</Prtry>

**P260**                         </MktInfrstrctrId>

**P261**                     </SysId>

**P262**                 </Svc>

**P263**                 <InvcDt>2019-01-31</InvcDt>

**P264**                 <BllgId>BILLINGID00002</BllgId>

**P265**                 <BllgPrd>

**P266**                     <FrDt>2019-01-01</FrDt>

**P267**                     <ToDt>2019-01-31</ToDt>

**P268**                 </BllgPrd>

**P269**                 <RspnsblPtyId>

**P270**                     <Id>

**P271**                         <AnyBIC>BITAITRRXXX</AnyBIC>

**P272**                     </Id>

**P273**                 </RspnsblPtyId>

**P274**                 <PtyId>

**P275**                     <Id>

**P276**                         <AnyBIC>UNCRITMMXXX</AnyBIC>

**P277**                     </Id>

**P278**                 </PtyId>

**P279**                 <InvcTtls>

**P280**                     <Tax>

**P281**                         <Rate>10</Rate>

**P282**                         <Desc>VAT</Desc>

**P283**                         <TaxblAmt Ccy="EUR">60.00</TaxblAmt>

**P284**                         <Amt Ccy="EUR">6.00</Amt>

**P285**                     </Tax>

**P286**                     <TtlInvcAmt>

**P287**                         <Amt Ccy="EUR">66.00</Amt>

**P288**                     </TtlInvcAmt>

**P289**                     <PmtDueDt>2019-02-20</PmtDueDt>

**P290**                 </InvcTtls>

**P291**                 <SvcCtgyTtls>

**P292**                     <TtlInvcAmt>

**P293**                         <Amt Ccy="EUR">60.00</Amt>

**P294**                     </TtlInvcAmt>

**P295**                     <SvcCtgy>

**P296**                         <Cd>SETT</Cd>

**P297**                     </SvcCtgy>

**P298**                     <SvcItmTtls>

**P299**                         <ItmTp>0001</ItmTp>

**P300**                         <Qty>1000</Qty>

**P301**                         <UnitPric Ccy="EUR">0.03</UnitPric>

**P302**                         <TtlInvcAmt>

**P303**                             <Amt Ccy="EUR">30.00</Amt>

**P304**                         </TtlInvcAmt>

**P305**                     </SvcItmTtls>

**P306**                     <SvcItmTtls>

**P307**                         <ItmTp>0002</ItmTp>

**P308**                         <Qty>200</Qty>

**P309**                         <UnitPric Ccy="EUR">0.15</UnitPric>

**P310**                         <TtlInvcAmt>

**P311**                             <Amt Ccy="EUR">30.00</Amt>

**P312**                         </TtlInvcAmt>

**P313**                     </SvcItmTtls>

**P314**                 </SvcCtgyTtls>

**P315**             </BllgRpt>

**P316**         </BllgRptOrErr>

**P317** </BllgRpt>

