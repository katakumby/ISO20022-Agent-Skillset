---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.18 OriginalTransactionReference <OrgnlTxRef>", "2.4.3.18.7 SettlementInformation <SttlmInf>"]
file_pages: [51, 52]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.18.7 SettlementInformation <SttlmInf>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 51 to 52.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 51

```text
CreditorSchemeIdentification <CdtrSchmeId> contains the following elements (see
"PartyIdentification272" on page 1193 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 1194
   PostalAddress <PstlAdr> [0..1] ± 1195
   Identification <Id> [0..1]  1195
{Or     OrganisationIdentification <OrgId> [1..1]  1196
       AnyBIC <AnyBIC> [0..1] IdentifierSet C4 1197
       LEI <LEI> [0..1] IdentifierSet 1197
       Other <Othr> [0..*]  1197
         Identification <Id> [1..1] Text 1198
         SchemeName <SchmeNm> [0..1]  1198
{Or           Code <Cd> [1..1] CodeSet 1198
Or}           Proprietary <Prtry> [1..1] Text 1198
         Issuer <Issr> [0..1] Text 1198
Or}     PrivateIdentification <PrvtId> [1..1]  1198
       DateAndPlaceOfBirth <DtAndPlcOfBirth> [0..1]  1199
         BirthDate <BirthDt> [1..1] Date 1199
         ProvinceOfBirth <PrvcOfBirth> [0..1] Text 1199
         CityOfBirth <CityOfBirth> [1..1] Text 1200
         CountryOfBirth <CtryOfBirth> [1..1] CodeSet C10 1200
       Other <Othr> [0..*]  1200
         Identification <Id> [1..1] Text 1200
         SchemeName <SchmeNm> [0..1]  1200
{Or           Code <Cd> [1..1] CodeSet 1201
Or}           Proprietary <Prtry> [1..1] Text 1201
         Issuer <Issr> [0..1] Text 1201
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C10 1201
   ContactDetails <CtctDtls> [0..1] ± 1201
2.4.3.18.7  SettlementInformation <SttlmInf>
Presence: [0..1]
Definition: Specifies the details on how the settlement of the original transaction(s) between the
instructing agent and the instructed agent was completed.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
51 March 2026
```

## File page 52

```text
Impacted by: C17 "InstructedReimbursementAgentAccountRule", C18
"InstructingReimbursementAgentAccountRule", C24 "SettlementMethodAgentRule", C25
"SettlementMethodClearingRule", C26 "SettlementMethodCoverAgentRule", C27
"SettlementMethodCoverRule", C32 "ThirdReimbursementAgentAccountRule", C33
"ThirdReimbursementAgentRule"
SettlementInformation <SttlmInf> contains the following SettlementInstruction15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementMethod <SttlmMtd> [1..1] CodeSet 53
   SettlementAccount <SttlmAcct> [0..1] ± C16,
C15
54
   ClearingSystem <ClrSys> [0..1]  54
{Or     Code <Cd> [1..1] CodeSet 55
Or}     Proprietary <Prtry> [1..1] Text 55
   InstructingReimbursementAgent <InstgRmbrsmntAgt> [0..1] ± 55
   InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C16,
C15
56
   InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 56
   InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C16,
C15
57
   ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 58
   ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C16,
C15
58
Constraints
• InstructedReimbursementAgentAccountRule
If InstructedReimbursementAgentAccount is present, then InstructedReimbursementAgent must be
present.
On Condition
    /InstructedReimbursementAgent is absent
Following Must be True
    /InstructedReimbursementAgentAccount Must be absent
• InstructingReimbursementAgentAccountRule
If InstructingReimbursementAgentAccount is present, then InstructingReimbursementAgent must be
present.
On Condition
    /InstructingReimbursementAgent is absent
Following Must be True
    /InstructingReimbursementAgentAccount Must be absent
• SettlementMethodAgentRule
If SettlementMethod is equal to INDA or INGA, then ReimbursementAgent(s) and ClearingSystem
are not allowed.
On Condition
    /SettlementMethod is equal to value 'InstructingAgent'
 Or    /SettlementMethod is equal to value 'InstructedAgent'
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
52 March 2026
```

