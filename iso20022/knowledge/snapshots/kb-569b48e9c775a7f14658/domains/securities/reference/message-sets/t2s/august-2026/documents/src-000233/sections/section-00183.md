---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["14 camt.076.001.01 BillingReportRequestV01", "14.4 Message Building Blocks", "14.4.2 SearchCriteria <SchCrit>", "14.4.2.1 Service <Svc>"]
file_pages: [236]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.076.001.01"]
---

# 14.4.2.1 Service <Svc>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 236 to 236.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 236

```text
SearchCriteria <SchCrit> contains the following BillingSearchCriteria3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Service <Svc> [0..1]  236
     SystemIdentification <SysId> [1..1] ± 236
     SystemCurrency <SysCcy> [0..1] CodeSet C1 236
   BillingIdentification <BllgId> [0..1] Text 237
   BillingPeriod <BllgPrd> [0..1] ± 237
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 237
   PartyIdentification <PtyId> [0..1] ± 237
   AccountIdentification <AcctId> [0..1]  238
{Or     SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 238
Or}     CashAccountIdentification <CshAcctId> [1..1] ± 238
14.4.2.1  Service <Svc>
Presence: [0..1]
Definition: Identification of the service or system for which the billing information must be returned.
Service <Svc> contains the following SystemAndCurrency1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentification <SysId> [1..1] ± 236
   SystemCurrency <SysCcy> [0..1] CodeSet C1 236
14.4.2.1.1  SystemIdentification <SysId>
Presence: [1..1]
Definition: Unique and unambiguous identification of the system, as assigned by the system
administrator.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 3203 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 3203
Or}   Country <Ctry> [1..1] CodeSet C3 3203
14.4.2.1.2  SystemCurrency <SysCcy>
Presence: [0..1]
Definition: Currency which may be processed by the system. A system may process transactions in a
single currency or in multiple currencies.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.076.001.01 BillingReportRequestV01
Target2-Securities 236 August 2026
```

