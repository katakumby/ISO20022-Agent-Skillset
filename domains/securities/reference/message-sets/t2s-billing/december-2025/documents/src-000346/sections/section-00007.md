---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["2 camt.076.001.01 BillingReportRequestV01", "2.4 Message Building Blocks", "2.4.2 SearchCriteria <SchCrit>", "2.4.2.1 Service <Svc>"]
file_pages: [7]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.076.001.01"]
---

# 2.4.2.1 Service <Svc>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 7 to 7.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 7

```text
SearchCriteria <SchCrit> contains the following BillingSearchCriteria3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Service <Svc> [0..1]  7
     SystemIdentification <SysId> [1..1] ± 7
     SystemCurrency <SysCcy> [0..1] CodeSet C1 7
   BillingIdentification <BllgId> [0..1] Text 8
   BillingPeriod <BllgPrd> [0..1] ± 8
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 8
   PartyIdentification <PtyId> [0..1] ± 8
   AccountIdentification <AcctId> [0..1]  9
{Or     SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 9
Or}     CashAccountIdentification <CshAcctId> [1..1] ± 9
2.4.2.1  Service <Svc>
Presence: [0..1]
Definition: Identification of the service or system for which the billing information must be returned.
Service <Svc> contains the following SystemAndCurrency1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentification <SysId> [1..1] ± 7
   SystemCurrency <SysCcy> [0..1] CodeSet C1 7
2.4.2.1.1  SystemIdentification <SysId>
Presence: [1..1]
Definition: Unique and unambiguous identification of the system, as assigned by the system
administrator.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 142
Or}   Country <Ctry> [1..1] CodeSet C3 142
2.4.2.1.2  SystemCurrency <SysCcy>
Presence: [0..1]
Definition: Currency which may be processed by the system. A system may process transactions in a
single currency or in multiple currencies.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.076.001.01 BillingReportRequestV01
Target2-Securities - Billing 7 December 2025
```

