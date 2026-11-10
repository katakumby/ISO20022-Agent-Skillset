---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.9 IntermediateSecurity <IntrmdtScty>"]
file_pages: [87]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.9 IntermediateSecurity <IntrmdtScty>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 87 to 87.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 87

```text
UnaffectedBalance <UafctdBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
3.4.9 IntermediateSecurity <IntrmdtScty>
Presence: [0..1]
Definition: Details on rights credited to the account as for example trading period, expiry date,
renounceability.
IntermediateSecurity <IntrmdtScty> contains the following FinancialInstrumentAttributes139
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecurityIdentification <SctyId> [1..1] ± C23,
C24,
C61,
C62,
C91
87
   Quantity <Qty> [0..1] Quantity 88
   RenounceableEntitlementStatusType
<RnncblEntitlmntStsTp>
[0..1] ± 89
   FractionDisposition <FrctnDspstn> [0..1] ± 89
   IntermediateSecuritiesToUnderlyingRatio
<IntrmdtSctiesToUndrlygRatio>
[0..1] ± 89
   MarketPrice <MktPric> [0..1] ± 89
   ExpiryDate <XpryDt> [1..1] ± 90
   PostingDate <PstngDt> [1..1] ± 90
   TradingPeriod <TradgPrd> [0..1] ± 90
   UninstructedBalance <UinstdBal> [0..1] ± 91
   InstructedBalance <InstdBal> [0..1] ± 91
3.4.9.1  SecurityIdentification <SctyId>
Presence: [1..1]
Definition: Identifies the financial instrument.
Impacted by: C23 "DescriptionPresenceRule", C24 "DescriptionUsageRule", C61 "ISINGuideline", C62
"ISINPresenceRule", C91 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 87 February 2026
```

